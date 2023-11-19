import Automated.pull as pull
import Database._class_structure_.Order as Order
import Database._class_structure_.Company as Company
import Database._class_structure_.Record as Record
import Database._class_structure_.PrintStatus as PrintStatus
import Database._class_structure_.FileInfo as FileInfo
import Database.Order_DB as Order_DB
import Database.Company_DB as Company_DB
from typing import List
import time, datetime, os, sys


def update_orders(source_company: Company.Company) -> None:
    # Get the data from the web server
    try:
        data = pull.pull_latest(source_company.api_key,
                                source_company.api_url)
        data = data.json()
    except Exception as e:
        print(f"Error: Couldn't pull data from {source_company.api_url} ({e})",
              file=sys.stderr)
        return

    company_id: int = Company_DB.get_company_id(source_company.company_name)
    
    # Parse the data
    pulled_data: List[Order.Order] = []
    for row in data:
        order_id = row[0]
        name_first = row[1]
        name_last = row[2]
        phone_number = row[3]
        shipping_address = row[4]
        tracking_number = row[5]
        received_datetime = datetime.datetime.now()

        pulled_data.append(Order.Order(order_id,
                                       received_datetime,
                                       name_first,
                                       name_last,
                                       phone_number,
                                       shipping_address,
                                       tracking_number,
                                       company_id,
                                       PrintStatus.PrintStatus.NOT_STARTED))

    # Add order to DB
    for item in pulled_data:
        # Send order to DB
        Order_DB.add_order(item)

        # Create sample file if it doesn't exist
        searched_order = Order_DB.find_order_by_customer_details(item.customer_name_first,
                                                                 item.customer_name_last,
                                                                 item.customer_shipping_address)
        data_dir = os.path.join(os.getcwd(), "data")
        file_extension = "pdf"
        order_label_file_name = f"label_{searched_order.order_id}.{file_extension}"
        order_label_file_path = os.path.join(data_dir, order_label_file_name)

        # Create a record with that order and print it
        try:
            os.mkdir(data_dir)
        except FileExistsError:
            pass
        
        file = open(order_label_file_path, "a")
        file.close()
        
        searched_company = Company_DB.find_company_by_id(company_id)
        record_fileinfo = FileInfo.FileInfo(order_label_file_name, data_dir)
        record_to_print = Record.Record(searched_company,
                                        record_fileinfo,
                                        PrintStatus.PrintStatus.NOT_STARTED,
                                        item)
        record_to_print.print_record()




def start_check(check_interval: int = 10) -> None:
    while True:
        # Get all the companies
        all_companies: List[Company.Company] = Company_DB.find_all_company()

        if all_companies == None:
            time.sleep(check_interval)
            continue

        # Fetch the records for all the companies
        for company in all_companies:
            if not company.is_enabled:
                continue

            print(f"Fetching orders and records from {company.api_url}")
            update_orders(company)
            
        time.sleep(check_interval)
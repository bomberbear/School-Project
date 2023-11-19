import pymysql, os, pathlib
import Database.Company_DB as Company_DB
import Database._class_structure_.Company as Company
import Database._class_structure_.Record as Record
import Database._class_structure_.PrintStatus as PrintStatus
import Database.Order_DB as Order_DB
import Database._class_structure_.FileInfo as FileInfo
from typing import List


def get_source():
    pass


def get_orders():
    orders = Order_DB.fetch_all_orders()
    return orders


def get_company():
    return Company_DB.find_all_company()


def compile_records():
    # Get info from db
    orders = get_orders()
    sources: List[Company.Company] = get_company()
    list_of_ids = []
    list_of_records = []
    for row in sources:
        company = []
        company.append(row.company_name)
        company.append(Company_DB.find_company_one_get_id(row.company_name))
        list_of_ids.append(company)

    # Create record object and append to list
    for order in orders:
        file_extension = "pdf"
        order_file_name = f"label_{order.order_id}.{file_extension}"
        matching_company = Company_DB.find_company_by_id(order.source_id)

        data_folder = os.path.join(os.getcwd(), "data")
        data_file = os.path.join(data_folder, order_file_name)
        data_file_size = 0

        if os.path.exists(data_file):
            data_file_obj = pathlib.Path(data_file)
            data_file_size = data_file_obj.stat().st_size

        file_info = FileInfo.FileInfo(order_file_name,
                                      data_folder,
                                      data_file_size)


        current_record = Record.Record(matching_company,
                                       file_info,
                                       order.printstatus,
                                       order)
        list_of_records.append(current_record)


    return list_of_records



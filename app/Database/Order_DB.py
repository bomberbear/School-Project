import pymysql, sys
import Database.DBInfo as DBInfo
import Database._class_structure_.Order as Order
import Database._class_structure_.PrintStatus as PrintStatus


def find_order_one(id):
    class QueryClass:
        Table = "Order"

    query = f"SELECT * FROM `{QueryClass.Table}` WHERE id = %s"

    # Class that stores the creds to connect
    db_info = DBInfo.DB()

    # Open database connection
    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (id,))

            # Fetch all the rows
            rows = cursor.fetchall()
            order_object = None

            # Process the rows
            for row in rows:
                print(row)
                order_object = Order.Order(row[0], row[7], row[2], row[3], row[4], row[5], row[6], row[1], row[8])

            return order_object
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def fetch_all_orders():
    query = "SELECT * FROM `Order`"

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query)

            # Fetch all the rows
            rows = cursor.fetchall()

            # Process the rows and create Order objects
            orders = [Order.Order(row[0], row[7], row[2], row[3], row[4], row[5], row[6], row[1], row[8]) for row in rows]
            return orders
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)
        exit(1)


def add_order(order):
    query = "INSERT INTO `Order` (source_id, received, firstName, lastName, phone, address, trackingNumber, printstatus) VALUES (%s, CURRENT_TIMESTAMP, %s, %s, %s, %s, %s, 'Not started')"

    # Replace the column names with the actual column names in your table
    data = (order.source_id, order.customer_name_first, order.customer_name_last, order.customer_phone_number,
            order.customer_shipping_address, order.tracking_number)

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, data)
            db.commit()
            print(f"Order {order.tracking_number} added successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def update_order(api_key_id, **kwargs):
    query = "UPDATE `Order` SET "
    update_columns = []
    update_values = []

    for column, value in kwargs.items():
        if column.lower() != 'id':
            update_columns.append(f"{column} = %s")
            update_values.append(value)

    if not update_columns:
        print("No valid columns provided to update.")
        return

    query += ', '.join(update_columns) + " WHERE ID = %s"
    update_values.append(api_key_id)

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, tuple(update_values))
            db.commit()
            print(f"API key with ID {api_key_id} updated successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def remove_order(order_id):
    query = "DELETE FROM `Order` WHERE ID = %s"

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (order_id,))
            db.commit()
            print(f"Order with ID {order_id} removed successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)

def find_order_by_customer_details(first_name, last_name, address) -> Order.Order:
    class QueryClass:
        Table = "Order"

    query = f"SELECT * FROM `{QueryClass.Table}` WHERE firstName = %s AND lastName = %s AND address = %s"

    # full_name = f"{first_name} {last_name}"

    # Class that stores the creds to connect
    db_info = DBInfo.DB()

    # Open database connection
    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (first_name, last_name, address))

            # Fetch all the rows
            rows = cursor.fetchall()
            order_object = None

            # Process the rows
            for row in rows:
                order_id = row[0]
                source_id = row[1]
                name_first = row[2]
                name_last = row[3]
                phone_num = row[4]
                address = row[5]
                tracking = row[6]
                received = row[7]
                print_status = row[8]

                order_object = Order.Order(order_id,
                                           received,
                                           name_first,
                                           name_last,
                                           phone_num,
                                           address,
                                           tracking,
                                           source_id,
                                           PrintStatus.str_to_printstatus(print_status))

            return order_object
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)

# setup = find_order_one(1)
# print(setup.printstatus)
# #
# setup.customer_name_first = "Test4"
# setup.customer_id = 5
# add_order(setup)

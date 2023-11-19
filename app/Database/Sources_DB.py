import pymysql, sys
import Database.DBInfo as DBInfo
import Database.Source_Class as Source


def find_source_one(name):
    class QueryClass:
        Table = "Source"

    query = f"SELECT * FROM {QueryClass.Table} WHERE name = %s"

    # Class that stores the creds to connect
    db_info = DBInfo.DB()

    # Open database connection
    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (name,))

            # Fetch all the rows
            rows = cursor.fetchall()
            source_object = None

            # Process the rows
            for row in rows:
                source_object = Source.Source(row[1], row[2], row[3], row[4], row[5], row[6], row[7])

            return source_object
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def find_source_by_name(name: str) -> int:
    class QueryClass:
        Table = "Company"

    query = f"SELECT DISTINCT source_id FROM {QueryClass.Table} WHERE name = %s"

    # Class that stores the creds to connect
    db_info = DBInfo.DB()

    # Open database connection
    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (name,))

            # Fetch all the rows
            response = cursor.fetchall()

            return response
        
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)



def fetch_all_sources():
    query = "SELECT * FROM `Source`"

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

            # Process the rows and create Source objects
            sources = [Source.Source(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]

            return sources
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def update_sources(sources_key_id, **kwargs):
    query = "UPDATE Source SET "
    update_columns = []
    update_values = []

    for column, value in kwargs.items():
        if column.lower() != 'id':
            update_columns.append(f"{column} = %s")
            update_values.append(value)

    if not update_columns:
        print("No valid columns provided to update.")
        return

    query += ', '.join(update_columns) + " WHERE SID = %s"
    update_values.append(sources_key_id)

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, tuple(update_values))
            db.commit()
            print(f"Sources key with ID {sources_key_id} updated successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def insert_source(source):
    query = """INSERT INTO `Source` (customerName, shippiongChoice, itemsSelected, sourceCompany, customerContactinfo, customerAddress, pdfLabel)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    # Replace the column names with the actual column names in your table
    data = (source.name, source.column2, source.column3, source.column4, source.column5, source.column6, source.column7)

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, data)
            db.commit()
            print("Source added successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def remove_source(source_id):
    query = "DELETE FROM `Source` WHERE sid = %s"

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (source_id,))
            db.commit()
            print(f"Source with ID {source_id} removed successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base",
              file=sys.stderr)


def get_sid_by_customer_name_and_address(customer_name, customer_address):
    query = "SELECT sid FROM `Source` WHERE customerName = %s AND customerAddress = %s"

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (customer_name, customer_address))

            # Fetch the first row
            row = cursor.fetchone()

            if row is not None:
                return row[0]
            else:
                print("No matching record found.")
                return None
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)

import pymysql, sys
import Database.DBInfo as DBInfo
import Database.Company as table


def find_company_one(name):
    class QueryClass:
        Name = name
        Table = "Company"

    query = f"SELECT * FROM {QueryClass.Table} WHERE Name = %s"

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
            api_key_object = None

            # Process the rows
            for row in rows:
                api_key_object = table.Company(row[1], row[2], row[3], row[4])

            return api_key_object
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)
        

def get_company_id(name: str) -> int:
    class QueryClass:
        Table = "Company"

    query = f"SELECT id FROM {QueryClass.Table} WHERE name = %s"

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

            return response[0][0]
        
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def find_company_by_id(id: int):
    query = "SELECT * FROM Company WHERE id = %s"
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

            # Process the rows
            api_key_object = None
            for row in rows:
                api_key_object = table.Company(row[1], row[2], row[3], row[4])

            return api_key_object
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def find_all_company():
    class QueryClass:
        Table = "Company"

    query = f"SELECT * FROM {QueryClass.Table}"

    # Class that stores the creds to connect
    db_info = DBInfo.DB()

    # Open database connection
    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query)

            # Fetch all the rows
            rows = cursor.fetchall()
            api_key_objects = []

            # Process the rows
            for row in rows:
                api_key_object = table.Company(row[1], row[2], row[4], row[3])
                api_key_objects.append(api_key_object)

            return api_key_objects
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def add_company(api_key):
    class QueryClass:
        Table = "Company"

    query = "INSERT INTO " + QueryClass.Table + " (Name, Enabled, Api_Key, URL) VALUES (%s, %s, %s, %s)"

    # Replace the column names with the actual column names in your table
    data = (api_key.company_name,
            api_key.is_enabled,
            api_key.api_key,
            api_key.api_url)

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, data)
            db.commit()
            print("API key added successfully.")
            return "Success"
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def add_manny_company(api_keys):
    class QueryClass:
        Table = "Company"

    query = "INSERT INTO " + QueryClass.Table + " (Name, Enabled, Api_Key, URL) VALUES (%s, %s, %s, %s)"

    data = [(api_key.column1, api_key.column2, api_key.column3, api_key.column4, api_key.column5) for api_key in
            api_keys]

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.executemany(query, data)
            db.commit()
            print(f"{len(api_keys)} API keys added successfully.")
            return "Success"
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def update_company(api_key_id, **kwargs):
    query = "UPDATE Company SET "
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


def remove_company(api_key_name):
    query = "DELETE FROM Company WHERE Name = %s"

    db_info = DBInfo.DB()

    try:
        with pymysql.connect(host=db_info.host,
                             user=db_info.user,
                             password=db_info.password,
                             database=db_info.database) as db:
            cursor = db.cursor()
            cursor.execute(query, (api_key_name,))
            db.commit()
            print(f"API key with ID {api_key_name} removed successfully.")
    except pymysql.err.OperationalError as e:
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)


def find_company_one_get_id(name):
    class QueryClass:
        Name = name
        Table = "Company"

    query = f"SELECT * FROM {QueryClass.Table} WHERE Name = %s"

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
            api_key_object = None

            # Process the rows
            for row in rows:
                api_key_object = row[0]

            return api_key_object
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)

# Example of doing the updates
# update_api_key(5, Name="Name44")

#print(find_all_api_keys())

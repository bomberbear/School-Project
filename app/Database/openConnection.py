import pymysql, DBInfo, sys

def TestDBConnection():
    # Class that stores the creds to connect
    db = DBInfo.DB
    # Open database connection
    try:
        db = pymysql.connect(host=db1.host,
                             user=db1.user,
                             password=db1.password,
                             database=db1.database)
        # Success message
        print("Connected to DB successfully!")
    except pymysql.err.OperationalError as e:
        # Error message
        print(f"Connection failed to data base: {e}",
              file=sys.stderr)
        #exit()
    db.close()

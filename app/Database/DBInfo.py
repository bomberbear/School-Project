class DB:
    def __init__(self, host="localhost", user="root", password="rootpassword", database="customers"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
class User:
    def __init__(self, user_name="", password="", email=""):
        self._user_name = user_name
        self._password = password
        self._email = email

    # User Name
    def get_user_name(self):
        return self._user_name

    def set_user_name(self, user_name):
        self._user_name = user_name

    # Password
    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    # Email
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

def accessLocalFolder():
    pass

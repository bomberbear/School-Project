class Order:
    def __init__(self,
                 uuid=0,
                 first_name="",
                 last_name="",
                 phone="",
                 address="",
                 tracking_address=""):
        self._uuid = uuid
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone
        self._address = address
        self._tracking_address = tracking_address

    # UUID
    def get_uuid(self):
        return self._uuid

    def set_uuid(self, uuid):
        self._uuid = uuid

    # First Name
    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    # Last Name
    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    # Phone
    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    # Address
    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    # Tracking Address
    def get_tracking_address(self):
        return self._tracking_address

    def set_tracking_address(self, tracking_address):
        self._tracking_address = tracking_address



def sendEmailNotifcation():
    pass

def sendToPDFToPrinter():
    pass

def savePDFToLocalFolder():
    pass
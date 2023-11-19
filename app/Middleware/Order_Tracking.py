class OrderTrackingInfo:
    def __init__(self,
                 source,
                 tracking_address,
                 email_status,
                 file_format,
                 print_status,
                 received_datetime,
                 order_id):
        self._order_id = order_id
        self.received_datetime = received_datetime
        self.source = source
        self.tracking_address = tracking_address
        self.email_status = email_status
        self.file_format = file_format
        self.print_status = print_status

    @property
    def received_datetime(self):
        return self._received_datetime

    @received_datetime.setter
    def received_datetime(self, value):
        self._received_datetime = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    @property
    def tracking_address(self):
        return self._tracking_address

    @tracking_address.setter
    def tracking_address(self, value):
        self._tracking_address = value

    @property
    def email_status(self):
        return self._email_status

    @email_status.setter
    def email_status(self, value):
        self._email_status = value

    @property
    def file_format(self):
        return self._file_format

    @file_format.setter
    def file_format(self, value):
        self._file_format = value

    @property
    def file_link(self):
        return self._file_link

    @file_link.setter
    def file_link(self, value):
        self._file_link = value

    @property
    def print_status(self):
        return self._print_status

    @print_status.setter
    def print_status(self, value):
        self._print_status = value

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value

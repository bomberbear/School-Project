from datetime import datetime

class Order:
    def __init__(self, order_id: int, received_datetime: datetime, 
                 customer_name_first: str, customer_name_last: str, 
                 customer_phone_number: str, customer_shipping_address: str, 
                 tracking_number: str, source_id: int, printstatus: str):
        self._order_id = order_id
        self._source_ID = source_id
        self._received_datetime = received_datetime
        self._customer_name_first = customer_name_first
        self._customer_name_last = customer_name_last
        self._customer_phone_number = customer_phone_number
        self._customer_shipping_address = customer_shipping_address
        self._tracking_number = tracking_number
        self._printstatus = printstatus
    # Getters
    @property
    def order_id(self):
        return self._order_id
    
    @property
    def received_datetime(self):
        return self._received_datetime
    
    @property
    def customer_name_first(self):
        return self._customer_name_first
    
    @property
    def customer_name_last(self):
        return self._customer_name_last
    
    @property
    def customer_phone_number(self):
        return self._customer_phone_number
    
    @property
    def customer_shipping_address(self):
        return self._customer_shipping_address
    
    @property
    def tracking_number(self):
        return self._tracking_number

    @property
    def source_id(self):
        return self._source_ID

    @property
    def printstatus(self):
        return self._printstatus

    # Setters
    @order_id.setter
    def order_id(self, value: int):
        self._order_id = value
    
    @received_datetime.setter
    def received_datetime(self, value: datetime):
        self._received_datetime = value
    
    @customer_name_first.setter
    def customer_name_first(self, value: str):
        self._customer_name_first = value
    
    @customer_name_last.setter
    def customer_name_last(self, value: str):
        self._customer_name_last = value
    
    @customer_phone_number.setter
    def customer_phone_number(self, value: str):
        self._customer_phone_number = value
    
    @customer_shipping_address.setter
    def customer_shipping_address(self, value: str):
        self._customer_shipping_address = value
    
    @tracking_number.setter
    def tracking_number(self, value: str):
        self._tracking_number = value

    @source_id.setter
    def source_id(self, value: str):
        self._source_ID = value

    @printstatus.setter
    def printstatus(self, value: str):
        self._printstatus = value
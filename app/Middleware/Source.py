class Source:
    def __init__(self, customer_name="", shipping_choice="", items_selected="", source_company="", customer_contactinfo="", customer_address="", pdf_label=""):
        self._customer_name = customer_name
        self._shipping_choice = shipping_choice
        self._items_selected = items_selected
        self._source_company = source_company
        self._customer_contactinfo = customer_contactinfo
        self._customer_address = customer_address
        self._pdf_label = pdf_label

    # Customer Name
    def get_customer_name(self):
        return self._customer_name

    def set_customer_name(self, customer_name):
        self._customer_name = customer_name

    # Shipping Choice
    def get_shipping_choice(self):
        return self._shipping_choice

    def set_shipping_choice(self, shipping_choice):
        self._shipping_choice = shipping_choice

    # Items Selected
    def get_items_selected(self):
        return self._items_selected

    def set_items_selected(self, items_selected):
        self._items_selected = items_selected

    # Source Company
    def get_source_company(self):
        return self._source_company

    def set_source_company(self, source_company):
        self._source_company = source_company

    # Customer Contact Info
    def get_customer_contactinfo(self):
        return self._customer_contactinfo

    def set_customer_contactinfo(self, customer_contactinfo):
        self._customer_contactinfo = customer_contactinfo

    # Customer Address
    def get_customer_address(self):
        return self._customer_address

    def set_customer_address(self, customer_address):
        self._customer_address = customer_address

    # PDF Label
    def get_pdf_label(self):
        return self._pdf_label

    def set_pdf_label(self, pdf_label):
        self._pdf_label = pdf_label

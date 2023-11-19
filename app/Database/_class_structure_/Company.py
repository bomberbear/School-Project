class Company:
    def __init__(self, company_name: str, is_enabled: bool, api_url: str, api_key: str):
        self._company_name = company_name
        self._is_enabled = is_enabled
        self._api_url = api_url
        self._api_key = api_key
    
    # Getters
    @property
    def company_name(self):
        return self._company_name
    
    @property
    def is_enabled(self):
        return self._is_enabled
    
    @property
    def api_url(self):
        return self._api_url
    
    @property
    def api_key(self):
        return self._api_key
    
    # Setters
    @company_name.setter
    def company_name(self, value: str):
        self._company_name = value
    
    @is_enabled.setter
    def is_enabled(self, value: bool):
        self._is_enabled = value
    
    @api_url.setter
    def api_url(self, value: str):
        self._api_url = value
    
    @api_key.setter
    def api_key(self, value: str):
        self._api_key = value
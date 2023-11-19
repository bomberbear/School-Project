class LocalFolder:
    def __init__(self, pdf_name="",
                 last_modified="",
                 location=""):
        self.pdf_name = pdf_name
        self.last_modified = last_modified
        self.location = location

    # Getters
    @property
    def pdf_name(self):
        return self._pdf_name

    @property
    def last_modified(self):
        return self._last_modified

    @property
    def location(self):
        return self._location
    
    # Setters
    @pdf_name.setter
    def pdf_name(self, pdf_name):
        self._pdf_name = pdf_name

    @last_modified.setter
    def last_modified(self, last_modified):
        self._last_modified = last_modified
    
    @location.setter
    def location(self, location):
        self._location = location
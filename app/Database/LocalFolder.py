class LocalFolder:
    def __init__(self, pdf_name="",
                 last_modified="",
                 location="",
                 file_size=0):
        self._pdf_name = pdf_name
        self._last_modified = last_modified
        self._location = location
        self._file_size = file_size

    # PDF Name
    def get_pdf_name(self):
        return self._pdf_name

    def set_pdf_name(self, pdf_name):
        self._pdf_name = pdf_name

    # Last Modified
    def get_last_modified(self):
        return self._last_modified

    def set_last_modified(self, last_modified):
        self._last_modified = last_modified

    # Location
    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    # File Size
    def get_file_size(self):
        return self._file_size

    def set_file_size(self, file_size):
        self._file_size = file_size

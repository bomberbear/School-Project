import os, psutil, subprocess, platform, sys
from time import sleep
from Database.Company import Company
from Database import Order_DB
from .FileInfo import FileInfo
from .PrintStatus import PrintStatus
from .Order import Order


class Record:
    def __init__(self, source_company: Company,
                 file_info: FileInfo,
                 print_status: PrintStatus,
                 order_details: Order
                 ):
        self._source_company = source_company
        self._file_info = file_info
        self._print_status = print_status
        self._order_details = order_details

    # Getters
    @property
    def source_company(self):
        return self._source_company

    @property
    def file_info(self):
        return self._file_info

    @property
    def print_status(self):
        return self._print_status

    @property
    def order_details(self):
        return self._order_details

    # Setters
    @source_company.setter
    def source_company(self, value: Company):
        self._source_company = value

    @file_info.setter
    def file_info(self, value: FileInfo):
        self._file_info = value

    @print_status.setter
    def print_status(self, value: PrintStatus):
        self._print_status = value

    @order_details.setter
    def order_details(self, value: Order):
        self._order_details = value


    def print_record(self) -> None:
        """
        Prints a PDF file from the filepath
        """
        # Set print status to In Progress
        self.order_details.printstatus = PrintStatus.IN_PROGRESS

        filepath = os.path.join(self.file_info.file_location, self.file_info.file_name)

        if platform.system() == "Windows":
            try:
                os.startfile(filepath, "print")
                sleep(5)
                for p in psutil.process_iter(): #Close PDF viewer after printing the PDF
                    if 'AcroRd' in str(p):
                        p.kill()
                self.order_details.printstatus = PrintStatus.SUCCESS

            except Exception as e:
                print(f"Could not print file: {e}",
                    file=sys.stderr)
                self.order_details.printstatus = PrintStatus.FAILURE

            # Add this line to close the py window automatically
            subprocess.call('TASKKILL /F /IM python.exe', shell=True)

        if platform.system() == "Linux":
            command = "lp"
            try:
                subprocess.call([command, filepath])
                self.order_details.printstatus = PrintStatus.SUCCESS
            except Exception as e:
                print(f"Could not print file: {e}",
                    file=sys.stderr)
                self.order_details.printstatus = PrintStatus.FAILURE

        Order_DB.update_order(self.order_details.order_id,
                              printstatus=str(self.order_details.printstatus))
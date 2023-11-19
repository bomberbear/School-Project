import os, psutil, subprocess, platform, sys
from time import sleep

class FileInfo:
    def __init__(self, file_name: str = "label_x.pdf", 
                 file_location: str = os.path.join(os.getcwd(), "data"), 
                 file_size: int = 0):
        self._file_name = file_name
        self._file_location = file_location     # path to containing folder
        self._file_size = file_size             # size in bytes
    
    # Getters
    @property
    def file_name(self):
        return self._file_name
    
    @property
    def file_location(self):
        return self._file_location
    
    @property
    def file_size(self):
        return self._file_size
    
    # Setters
    @file_name.setter
    def file_name(self, value: str):
        self._file_name = value
    
    @file_location.setter
    def file_location(self, value: str):
        self._file_location = value
    
    @file_size.setter
    def file_size(self, value: int):
        self._file_size = value


    def view_file(self) -> None:
        """
        Opens the pdf in default viewer
        """
        file_path = os.path.join(self.file_location, self.file_name)

        print(f"Opening file for viewing: {file_path}")

        if platform.system() == "Windows":
            try:
                os.startfile(file_path)
            except FileNotFoundError:
                print(f"Could not view file: File {file_path} could not be found.",
                    file=sys.stderr)

        if platform.system() == "Linux":
            command = "xdg-open"
            try:
                subprocess.call([command, file_path])
            except Exception as e:
                print(f"Could not view file: {e}",
                    file=sys.stderr)
    

    def print_pdf(self):
        """
        Prints a PDF file from the filepath
        """
        filepath = os.path.join(self.file_location, self.file_name)

        if platform.system() == "Windows":
            try:
                os.startfile(filepath, "print")
                sleep(5)
                for p in psutil.process_iter(): #Close PDF viewer after printing the PDF
                    if 'AcroRd' in str(p):
                        p.kill()
            except Exception as e:
                print(f"Could not print file: {e}",
                    file=sys.stderr)

            # Add this line to close the py window automatically
            subprocess.call('TASKKILL /F /IM python.exe', shell=True)

        if platform.system() == "Linux":
            command = "lp"
            try:
                subprocess.call([command, filepath])
            except Exception as e:
                print(f"Could not print file: {e}",
                    file=sys.stderr)
                
                
    def size_as_str(self) -> str:
        bytes = self.file_size
        
        sizes = ["bytes", "KB", "MB", "GB", "TB"]
        index = 0

        while bytes >= 1024 and index < len(sizes) - 1:
            bytes /= 1024
            index += 1

        return f"{bytes:.2f} {sizes[index]}"

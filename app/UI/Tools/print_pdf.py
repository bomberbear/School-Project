import os, psutil, subprocess, platform, sys
from time import sleep

def print_pdf(filepath):
    """
    Prints a PDF file from the filepath
    """
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
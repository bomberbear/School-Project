import UI.UI as main_ui
import Automated.update_orders as orders
import threading

"""
IMPORTANT: Run this from the folder "AutomatedLabelingSystem"!!!
Alternatively, run start.py in the directory above this one.
"""

def main():
    print("Starting Automated Labeling System...")
    
    # Begin API grabbing
    seconds_before_next_api_query = 60
    threading.Thread(target = orders.start_check, daemon=True, args=[seconds_before_next_api_query]).start()

    # Open main window
    main_window = main_ui.MainWindow().mainwindow
    main_window.mainloop()


if __name__ == "__main__":
    main()
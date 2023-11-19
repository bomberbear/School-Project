#!/usr/bin/python3
import os
from UI.Tools import get_paths as paths
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from typing import List
import sys
import UI.Colors as Colors
import UI.Misc as Misc
from Database import Company, Company_DB, Records_db, Order_DB
from Database._class_structure_ import Record, FileInfo, Order, PrintStatus
from UI.AddCompanyWizard import CompanyWizardWindow

# init global vars
assets_folder = paths.get_assets_folder()

# load button images
button_image_active_path = os.path.join(assets_folder, "button_active.png")
button_image_active_data = Image.open(button_image_active_path)

button_image_inactive_path = os.path.join(assets_folder, "button_inactive.png")
button_image_inactive_data = Image.open(button_image_inactive_path)

class MainWindow:
    def __init__(self, master=None, close_on_escape: bool=False):


        """
        Here lies the window configuration.
        """

        # build ui
        toplevel_1 = tk.Tk() if master is None else tk.Toplevel(master)
        
        # set icon
        img_path = os.path.join("app", "UI", "assets", "printer.png")
        self.img_printer = tk.PhotoImage(file=img_path)
        
        # configure window
        toplevel_1.title("Automated Labeling System")
        toplevel_1.configure(background=Colors.CustomColors.deep_green,
                             height=200,
                             width=200,
                             cursor="arrow")
        toplevel_1.iconphoto(True, self.img_printer)
        toplevel_1.minsize(1200, 700)
        
        toplevel_1.rowconfigure(0, minsize=80)
        toplevel_1.rowconfigure(1, minsize=500, weight=1)
        toplevel_1.rowconfigure(2, minsize=80)
        toplevel_1.columnconfigure(0, minsize=250)
        toplevel_1.columnconfigure(1, minsize=500, weight=1)
        toplevel_1.columnconfigure(2, minsize=80)


        """
        Here lies the title label along with the printer image.
        """

        # add title label
        title_label = ttk.Label(toplevel_1)
        title_label.configure(
            background=Colors.CustomColors.deep_green,
            font=("Chiller", 48, ""),
            foreground="white",
            justify="center",
            text='Automated\nLabeling\nSystem')
        title_label.grid(column=0, row=1, sticky="n")
        
        # add label printer image
        printer_image_opacity_scale = 0.5
        
        # printer_image_path = "app/UI/assets/label_printer_image_temp.png"
        printer_image_path = os.path.join("app", "UI", "assets", "label_printer_image_temp.png")
        printer_image = Image.open(printer_image_path)
        
        # change image opacity
        r, g, b, a = printer_image.split()
        printer_image_transparent = Image.merge("RGBA", (r, g, b, a.point(lambda i: i * printer_image_opacity_scale)))
        
        # show printer image
        label_printer_image = ttk.Label(toplevel_1)
        self.img_label_printer_image_temp = ImageTk.PhotoImage(printer_image_transparent)
        label_printer_image.configure(
            background=Colors.CustomColors.deep_green,
            image=self.img_label_printer_image_temp
            )
        label_printer_image.grid(column=0, row=1, rowspan=2, sticky="s")
        


        """
        Here lies the content the tabs will show.
        """
        
        # configure content frame
        self.content_frame = tk.Frame(toplevel_1)
        self.content_frame.configure(height=200,
                                     width=200,
                                     background=Colors.CustomColors.light_green,
                                     cursor="arrow")
        
        # set some vars for content inside content frame
        self.content_row = 0
        self.content_column = 0
        self.content_sticky = "nesw"
        self.content_padx = 50
        self.content_pady = (90, 50)

        # add content frame
        self.content_frame.grid(column=1, row=1, sticky="nsew")
        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.configure(cursor="arrow")

        # Create contents
        self.orders_content_frame = tk.Frame(self.content_frame)
        self.records_content_frame = tk.Frame(self.content_frame)
        self.settings_content_frame = tk.Frame(self.content_frame)

        # Set base configuration of content frame
        self.orders_content_frame.configure(bg=Colors.CustomColors.light_green, cursor="arrow")
        self.records_content_frame.configure(bg=Colors.CustomColors.light_green, cursor="arrow")
        self.settings_content_frame.configure(bg=Colors.CustomColors.light_green, cursor="arrow")

        # IMPORTANT: Frame row config and grid calls are placed lower

        # Set row configuration
        self.orders_content_frame.rowconfigure(0, weight=1)
        self.records_content_frame.rowconfigure(0, weight=1)
        self.settings_content_frame.rowconfigure(0, weight=1)
        
        # Set column configuration
        self.orders_content_frame.columnconfigure(0, weight=1)
        self.records_content_frame.columnconfigure(0, weight=1)
        self.settings_content_frame.columnconfigure(0, weight=1)

        
        """
        Here lies the tab buttons.
        """
        
        # set some button vars
        button_text_format = ("Calibri", 20, "bold")
        button_size_width = 200
        button_size_height = 65
        button_cursor = "hand2"
        button_place_x = 350
        button_place_y = 60
        button_padding = 225
        
        # Resize image to fit within button
        button_image_active_resized = button_image_active_data.resize((button_size_width, button_size_height))
        button_image_inactive_resized = button_image_inactive_data.resize((button_size_width, button_size_height))
        
        # Convert image format to tkinter type
        self.button_image_active = ImageTk.PhotoImage(button_image_active_resized)
        self.button_image_inactive = ImageTk.PhotoImage(button_image_inactive_resized)

        # Define the buttons
        self.orders_button = tk.Label(toplevel_1)
        self.records_button = tk.Label(toplevel_1)
        self.settings_button = tk.Label(toplevel_1)

        # set active tab
        self.active_button = self.orders_button

        # Configure the buttons
        self.orders_button.configure(cursor=button_cursor, 
                           text='Orders',
                           font=button_text_format,
                           bg=Colors.CustomColors.deep_green,
                           image=self.button_image_active if self.active_button == self.orders_button else self.button_image_inactive,
                           compound="center",
                           height=button_size_height,
                           width=button_size_width,
                           borderwidth=0)

        self.records_button.configure(cursor=button_cursor, 
                           text='Records',
                           font=button_text_format,
                           bg=Colors.CustomColors.deep_green,
                           image=self.button_image_active if self.active_button == self.records_button else self.button_image_inactive,
                           compound="center",
                           height=button_size_height,
                           width=button_size_width,
                           borderwidth=0)
        
        self.settings_button.configure(cursor=button_cursor, 
                           text='Settings',
                           font=button_text_format,
                           bg=Colors.CustomColors.deep_green,
                           image=self.button_image_active if self.active_button == self.settings_button else self.button_image_inactive,
                           compound="center",
                           height=button_size_height,
                           width=button_size_width,
                           borderwidth=0)

        # Bind the buttons
        self.orders_button.bind("<Enter>",
                                 self.orders_button_enter)
        self.orders_button.bind("<Leave>",
                                 self.orders_button_leave)
        self.orders_button.bind("<Button-1>",
                                 self.orders_button_clicked)
        
        self.records_button.bind("<Enter>",
                                 self.records_button_enter)
        self.records_button.bind("<Leave>",
                                 self.records_button_leave)
        self.records_button.bind("<Button-1>",
                                 self.records_button_clicked)
        
        self.settings_button.bind("<Enter>",
                                 self.settings_button_enter)
        self.settings_button.bind("<Leave>",
                                 self.settings_button_leave)
        self.settings_button.bind("<Button-1>",
                                 self.settings_button_clicked)
        
        # Place the buttons
        self.orders_button.place(x=button_place_x, y=button_place_y)
        self.records_button.place(x=button_place_x + button_padding, y=button_place_y)
        self.settings_button.place(x=button_place_x + (button_padding * 2), y=button_place_y)


        # Display contents if active
        match self.active_button:
            case self.orders_button:
                self.show_orders_content()
            
            case self.records_button:
                self.show_records_contents()
            
            case self.settings_button:
                self.show_settings_contents()
        

        """
        Here lies the Content Frame style configuration
        """
        
        # Create table styles
        self.table_style = ttk.Style()
        self.table_style_name = "Custom.Treeview"
        self.table_style.configure(self.table_style_name,
                                   background=Colors.CustomColors.light_green,
                                   rowheight=30)

        self.table_header_style = ttk.Style()
        self.table_header_style_name = "Custom.Treeview.Heading"
        self.table_header_style.configure(self.table_header_style_name,
                                          background=Colors.CustomColors.mid_green,
                                          padding=(0, 0),
                                          relief="flat")
        
        self.table_cell_style = ttk.Style()
        self.table_cell_style_name = "Custom.Treeview.Cell"
        self.table_cell_style.configure(self.table_cell_style_name,
                                        padding=(0, 0),
                                        borderwidth=2)
        
        
        """
        Here lies the table initialization
        """
        self.all_records: List[Record.Record] = Records_db.compile_records()
        self.all_companies: List[Company.Company] = Company_DB.find_all_company()
        
        # Need to at least define the treeviews for function first runs
        self.orders_table = ttk.Treeview(self.orders_content_frame)
        self.records_table = ttk.Treeview(self.records_content_frame)
        self.settings_table = ttk.Treeview(self.settings_content_frame)

        # Configure the tables and show them
        self.update_orders_table()
        self.update_records_table()
        self.update_settings_table()


        """
        Here lies the Settings "Add Company" button
        """
        self.add_company_button_height = 50
        self.add_company_button_width = 50

        self.add_company_image_path = os.path.join(assets_folder, "add_icon.png")
        self.add_company_image_data = Image.open(self.add_company_image_path)
        self.add_company_image_data.resize((75, 75))
        self.add_company_icon = ImageTk.PhotoImage(self.add_company_image_data)

        self.add_company_button = tk.Label(self.settings_content_frame)
        self.add_company_button.configure(cursor=button_cursor,
                                        #   text="",
                                          image=self.add_company_icon,
                                          bg=Colors.CustomColors.light_green,
                                          height=self.add_company_button_height,
                                          width=self.add_company_button_width,
                                          borderwidth=0)
        self.add_company_button.bind("<Button-1>",
                                     self.create_new_company)

        self.add_company_button.grid(column=0,
                                     row=1,
                                     sticky="se")
        

        """
        Here lies some misc stuff
        """
        
        # Display the content frames in grids
        match self.active_button:
            case self.orders_button:
                self.show_orders_content()
            
            case self.records_button:
                self.show_records_contents()
            
            case self.settings_button:
                self.show_settings_contents()

        # used for debugging
        if close_on_escape:
            toplevel_1.bind("<Escape>", self.close_window)

        # Main widget
        self.mainwindow = toplevel_1


    """
    Here lies the class functions
    """

    def run(self):
        self.mainwindow.mainloop()
        
    
    def close_window(self, event):
        print("Escape key pressed. Closing window...")
        self.mainwindow.destroy()
        

    def show_orders_content(self):
        self.orders_content_frame.grid(row=self.content_row,
                                 column=self.content_column,
                                 sticky=self.content_sticky,
                                 padx=self.content_padx,
                                 pady=self.content_pady)

        self.records_content_frame.grid_forget()
        self.settings_content_frame.grid_forget()

    
    def update_orders_table(self):
        print("Updating Orders table")
        self.orders_table.forget()


        """
        Here lies the Orders Frame contents
        """

        # Update all the records
        self.all_records: List[Record.Record] = Records_db.compile_records()

        # Create the table
        self.orders_columns = ["Received",
                               "Source",
                               "First Name",
                               "Last Name",
                               "Phone",
                               "Address",
                               "Tracking",
                               "Print Status"]
        self.orders_rows = len(self.all_records)
        self.orders_table = ttk.Treeview(self.orders_content_frame,
                                         columns=self.orders_columns,
                                         show="headings",
                                         style="Custom.Treeview")
        datetime_str_format = "%d/%m/%y %H:%M"
        self.orders_table.pack(side='left', fill='both', expand=True)
        
        # Set up column headings
        for col in self.orders_columns:
            self.orders_table.heading(col, text=col, anchor="w")
        
        for row_index in range(self.orders_rows):
            company_data = self.all_records[row_index].source_company
            row_data = [
                self.all_records[row_index].order_details.received_datetime.strftime(datetime_str_format),
                company_data.company_name if company_data != None else "Unknown",
                self.all_records[row_index].order_details.customer_name_first,
                self.all_records[row_index].order_details.customer_name_last,
                self.all_records[row_index].order_details.customer_phone_number,
                self.all_records[row_index].order_details.customer_shipping_address,
                self.all_records[row_index].order_details.tracking_number,
                self.all_records[row_index].print_status,
            ]
            
            self.orders_table.insert("", "end", values=row_data)
            
                    
        # Set column widths
        self.orders_table.column(self.orders_columns[0], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[1], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[2], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[3], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[4], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[5], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[6], width=100, minwidth=100)
        self.orders_table.column(self.orders_columns[7], width=100, minwidth=100)
        
        # Set background color of rows
        self.orders_table.tag_configure("even", background=Colors.CustomColors.light_green)
        self.orders_table.tag_configure("odd", background=Colors.CustomColors.lightest_green)
        for i, item_id in enumerate(self.orders_table.get_children()):
            tag = "even" if i % 2 == 0 else "odd"
            self.orders_table.item(item_id, tags=(tag,))
    

    def orders_button_clicked(self, event):
        print("Sources button pressed.")
        
        # Set active button
        self.active_button = self.orders_button

        # Set image for other buttons
        self.records_button.configure(image=self.button_image_inactive)
        self.settings_button.configure(image=self.button_image_inactive)

        # Show tab contents
        self.show_orders_content()

        # Update the orders table if it exists
        try:
            self.update_orders_table()
        except NameError:
            pass
    

    def orders_button_enter(self, event):
        self.orders_button.config(image=self.button_image_active)

    
    def orders_button_leave(self, event):
        if self.active_button != self.orders_button:
            self.orders_button.config(image=self.button_image_inactive)


    def show_records_contents(self):
        self.records_content_frame.grid(row=self.content_row,
                                 column=self.content_column,
                                 sticky=self.content_sticky,
                                 padx=self.content_padx,
                                 pady=self.content_pady)

        self.orders_content_frame.grid_forget()
        self.settings_content_frame.grid_forget()

    
    def update_records_table(self):
        print("Updating Records table")
        self.records_table.forget()

        """
        Here lies the Records Frame contents
        """

        # Update all the records
        self.all_records: List[Record.Record] = Records_db.compile_records()

        # Create the table
        self.records_columns = ["Source", "Print Status", "Containing Folder", "File Name", "File Size"]
        self.records_rows = len(self.all_records)
        self.records_table = ttk.Treeview(self.records_content_frame,
                                         columns=self.records_columns,
                                         show="headings",
                                         style="Custom.Treeview")
        self.records_table.pack(side='left', fill='both', expand=True)
        
        # Set up column headings
        for col in self.records_columns:
            self.records_table.heading(col, text=col, anchor="w")
        
        # Insert rows
        for row_index in range(self.records_rows):
            # Get the row data
            company_data = self.all_records[row_index].source_company
            row_data = [
                company_data.company_name if company_data != None else "Unknown",
                self.all_records[row_index].print_status,
                self.all_records[row_index].file_info.file_location,
                self.all_records[row_index].file_info.file_name,
                self.all_records[row_index].file_info.size_as_str()
            ]
            
            self.records_table.insert("", "end", values=row_data)
            self.records_table.bind("<Double-1>", self.open_record_file)
                    
        # Set column widths
        self.records_table.column(self.records_columns[0], width=100, minwidth=90)
        self.records_table.column(self.records_columns[1], width=100, minwidth=90)
        self.records_table.column(self.records_columns[2], width=100, minwidth=90)
        self.records_table.column(self.records_columns[3], width=60, minwidth=60)
        self.records_table.column(self.records_columns[4], width=100, minwidth=90)
        
        # Set background color of rows
        self.records_table.tag_configure("even", background=Colors.CustomColors.light_green)
        self.records_table.tag_configure("odd", background=Colors.CustomColors.lightest_green)
        for i, item_id in enumerate(self.records_table.get_children()):
            tag = "even" if i % 2 == 0 else "odd"
            self.records_table.item(item_id, tags=(tag,))


    def records_button_clicked(self, event):
        print("Orders button pressed.")
        
        # Set active button
        self.active_button = self.records_button

        # Set image for other buttons
        self.orders_button.configure(image=self.button_image_inactive)
        self.settings_button.configure(image=self.button_image_inactive)

        # Show tab contents
        self.show_records_contents()

        # Update the records table if it exists
        try:
            self.update_records_table()
        except NameError:
            pass
    
    
    def records_button_enter(self, event):
        self.records_button.config(image=self.button_image_active)
    

    def records_button_leave(self, event):
        if self.active_button != self.records_button:
            self.records_button.config(image=self.button_image_inactive)

        
    def show_settings_contents(self):
        self.settings_content_frame.grid(row=self.content_row,
                                 column=self.content_column,
                                 sticky=self.content_sticky,
                                 padx=self.content_padx,
                                 pady=self.content_pady)

        self.orders_content_frame.grid_forget()
        self.records_content_frame.grid_forget()

    
    def update_settings_table(self):
        print("Updating settings table.")
        self.settings_table.forget()


        """
        Here lies the Settings Frame contents
        """
        
        # Create the table
        self.settings_columns = ["Enabled", "Company Name", "API URL"]
        self.settings_rows = len(self.all_companies)
        self.settings_table = ttk.Treeview(self.settings_content_frame,
                                         columns=self.settings_columns,
                                         show="headings",
                                         style="Custom.Treeview")

        self.all_companies: List[Company.Company] = Company_DB.find_all_company()

        # Set up column headings
        for col in self.settings_columns:
            self.settings_table.heading(col, text=col, anchor="w")

        # Insert rows
        for row_index in range(self.settings_rows):
            # Get the row data
            row_data = [
                "Yes" if self.all_companies[row_index].is_enabled == "1" else "No",
                self.all_companies[row_index].company_name,
                self.all_companies[row_index].api_url
            ]
            
            item_id = self.settings_table.insert("", "end", values=row_data)
            self.settings_table.bind("<Double-1>", self.edit_selected_company)

        # self.settings_table.grid(side='left', fill='both', expand=True,
        #                          pady=(0, 30))
        self.settings_table.grid(row=0,
                                 column=0,
                                 sticky="nsew",
                                 pady=(0, 30))

        # Set column widths
        self.settings_table.column(self.settings_columns[0], width=10, minwidth=10)
        self.settings_table.column(self.settings_columns[1], width=200, minwidth=90)
        self.settings_table.column(self.settings_columns[2], width=150, minwidth=90)

        # Set background color of rows
        self.settings_table.tag_configure("even", background=Colors.CustomColors.light_green)
        self.settings_table.tag_configure("odd", background=Colors.CustomColors.lightest_green)
        for i, item_id in enumerate(self.settings_table.get_children()):
            tag = "even" if i % 2 == 0 else "odd"
            self.settings_table.item(item_id, tags=(tag,))
    

    def settings_button_clicked(self, event):
        print("Records button pressed.")
        
        # Set active button
        self.active_button = self.settings_button

        # Set image for other buttons
        self.orders_button.configure(image=self.button_image_inactive)
        self.records_button.configure(image=self.button_image_inactive)

        # Show tab contents
        self.show_settings_contents()

        # Update the settings table if it exists
        try:
            self.update_settings_table()
        except NameError:
            pass


    def settings_button_enter(self, event):
        self.settings_button.config(image=self.button_image_active)
    

    def settings_button_leave(self, event):
        if self.active_button != self.settings_button:
            self.settings_button.config(image=self.button_image_inactive)

    def edit_selected_company(self, event):
        # get selected row
        tree = event.widget
        focus = tree.focus()
        company_name = tree.item(focus)["values"][1]
        target_company: Company.Company = None

        # find corresponding company
        for item in self.all_companies:
            if item.company_name == company_name:
                target_company = item

        # input validation
        if target_company == None:
            print(f"Could not find company {company_name} in all_companies.",
                  file=sys.stderr)
            return

        print(f"Editing company {target_company.company_name}")
        company_window = CompanyWizardWindow(self.update_settings_table,
                                             master=self.mainwindow,    # Allows wizardwindow to inherit vars from MainWindow
                                             company_name=target_company.company_name,
                                             company_enabled=target_company.is_enabled,
                                             api_url=target_company.api_url,
                                             api_key=target_company.api_key)
        
        # Update the Treeview widget after
        company_window.mainwindow.mainloop()
    

    def open_record_file(self, event):
        # get selected row
        tree = event.widget
        focus = tree.focus()
        file_name = tree.item(focus)["values"][3]
        target_record: Record.Record = None

        # find corresponding record
        for item in self.all_records:
            if item.file_info.file_name == file_name:
                target_record = item

        # input validation
        if target_record == None:
            print(f"Could not find record with file name {file_name} in all_records.",
                  file=sys.stderr)
            return

        else:
            target_record.file_info.view_file()


    def create_new_company(self, event):
        print("Add Company button pressed.")
        print("Creating new company.")

        company_window = CompanyWizardWindow(self.update_settings_table,
                                             master=self.mainwindow)
        
        company_window.mainwindow.mainloop()


if __name__ == "__main__":
    
    app = MainWindow(close_on_escape=True)
    app.run()

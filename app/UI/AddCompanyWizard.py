#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from Database import Company_DB, Company

class CompanyWizardWindow:
    def __init__(self, update_func, master=None, company_name="", company_enabled=True, api_url="", api_key=""):
        self.update_func = update_func

        # Create window
        if master is None:
            self.wizard_window = tk.Tk()
        # Create window
        self.wizard_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.wizard_window.title("Add/Edit Company")
        self.wizard_window.configure(height=600, width=400)
        self.wizard_window.resizable(False, False)
        self.wizard_window.bind("<Escape>", self.close_window)
        self.wizard_window.bind("<Return>", self.return_key_pressed)
        
        # Create title
        self.title_frame = ttk.Frame(self.wizard_window)
        self.title_frame.configure(width=400)
        self.title_label = ttk.Label(self.title_frame)
        self.title_label.configure(
            font="{Calibri} 20 {bold}",
            text='Add / Edit Company')
        self.title_label.grid(column=0, row=0, sticky="w")
        self.title_frame.grid(column=0, padx=10, pady=15, row=0, sticky="nw")
        self.title_frame.columnconfigure(0, minsize=400)
        
        
        """
        Here lies the "Basic Info" section
        """
        
        # String vars
        self.original_company_name = company_name
        self.user_input_company_name = tk.StringVar(value=company_name)
        self.company_is_enabled = tk.BooleanVar(value=company_enabled)
        self.user_input_api_url = tk.StringVar(value=api_url)
        self.user_input_api_key = tk.StringVar(value=api_key)
        
        # Frame setup
        self.basic_info_section = ttk.Labelframe(self.wizard_window)
        self.basic_info_section.configure(
            padding=5, text='Basic Information', width=400)
        self.basic_info_section.rowconfigure(0, pad=5)
        self.basic_info_section.rowconfigure("all", pad=5)
        self.basic_info_section.columnconfigure(0, weight=1)
        self.basic_info_section.columnconfigure("all", weight=1)
        
        # row: Company Name
        self.company_name_label = ttk.Label(self.basic_info_section)
        self.company_name_label.configure(text='Company Name')
        self.company_name_label.grid(column=0, row=0, sticky="w")
        self.company_name_entry = ttk.Entry(self.basic_info_section)
        self.company_name_entry.configure(textvariable=self.user_input_company_name,
                                          width=30)
        self.company_name_entry.grid(column=1, row=0, sticky="e")
        
        # row: Company Enabled
        self.company_enabled_label = ttk.Label(self.basic_info_section)
        self.company_enabled_label.configure(text='Enabled')
        self.company_enabled_label.grid(column=0, row=2, sticky="w")
        self.company_enabled_check = ttk.Checkbutton(self.basic_info_section)
        self.company_enabled_check.configure(
            state="normal", variable=self.company_is_enabled)
        self.company_enabled_check.grid(
            column=1, padx="0 225", row=2, sticky="e")
        self.basic_info_section.grid(
            column=0, padx=10, pady=5, row=6, sticky="ew")
        
        
        """
        Here lies the "API Info" section
        """
        
        # Frame setup
        self.api_info_section = ttk.Labelframe(self.wizard_window)
        self.api_info_section.configure(
            padding=5, text='API Information', width=400)
        self.api_info_section.grid(
            column=0, padx=10, pady=5, row=7, sticky="ew")
        self.api_info_section.rowconfigure(0, pad=10)
        self.api_info_section.rowconfigure("all", pad=5)
        self.api_info_section.columnconfigure(0, weight=1)
        self.api_info_section.columnconfigure("all", weight=1)
        
        # row: API URL
        self.api_url_label = ttk.Label(self.api_info_section)
        self.api_url_label.configure(text='API URL')
        self.api_url_label.grid(column=0, row=0, sticky="w")
        self.api_url_entry = ttk.Entry(self.api_info_section)
        self.api_url_entry.configure(
            textvariable=self.user_input_api_url, width=30)
        self.api_url_entry.grid(column=1, row=0, sticky="e")
        
        # row: API Key
        self.api_key_label = ttk.Label(self.api_info_section)
        self.api_key_label.configure(text='API Key')
        self.api_key_label.grid(column=0, row=1, sticky="w")
        self.api_key_entry = ttk.Entry(self.api_info_section)
        self.api_key_entry.configure(
            textvariable=self.user_input_api_key, width=30)
        self.api_key_entry.grid(column=1, row=1, sticky="e")
        

        """
        Here lies the save buttons
        """
        
        # Save button
        self.save_options = ttk.Frame(self.wizard_window)
        self.save_options.configure(height=200, width=200)
        self.save_options.grid(
            column=0,
            padx="0 5",
            pady="15 7",
            row=100,
            sticky="se")
        
        # Ok button
        self.ok_button = ttk.Button(self.save_options, command=self.ok_button_pressed)
        self.ok_button.configure(text='Ok')
        self.ok_button.grid(column=0, padx=3, row=0)
        
        # Cancel button
        self.cancel_button = ttk.Button(self.save_options, command=self.cancel_button_pressed)
        self.cancel_button.configure(text='Cancel')
        self.cancel_button.grid(column=1, padx=3, row=0)
        
        # Apply button
        self.apply_button = ttk.Button(self.save_options, command=self.apply_button_pressed)
        self.apply_button.configure(text='Apply')
        self.apply_button.grid(column=2, padx=3, row=0)
        

        # Main widget
        self.mainwindow = self.wizard_window
        
        
    def return_key_pressed(self, event):
        print("Return key pressed.")
        self.print_entries()
        self.save_values()
        self.wizard_window.destroy()
    
    
    def ok_button_pressed(self):
        print("OK button pressed.")
        self.print_entries()
        self.save_values()
        self.wizard_window.destroy()
    
    
    def cancel_button_pressed(self):
        print("Cancel button pressed.")
        self.wizard_window.destroy()
        
    
    def apply_button_pressed(self):
        print("Apply button pressed.")
        self.print_entries()
        self.save_values()
    
    
    def save_values(self):
        local_company = Company.Company(self.company_name_entry.get(),
                                        self.company_is_enabled.get(),
                                        self.api_url_entry.get(),
                                        self.api_key_entry.get())
        db_company: Company.Company = Company_DB.find_company_one(self.original_company_name)
        
        if db_company == None and self.original_company_name == "":
            Company_DB.add_company(local_company)
        else:
            company_id = Company_DB.find_company_one_get_id(self.original_company_name)
            Company_DB.update_company(company_id,
                                      Name=local_company.company_name,
                                      Enabled=local_company.is_enabled,
                                      URL=local_company.api_url,
                                      Api_Key=local_company.api_key)
        
        self.update_func()
            
    
    def print_entries(self):
        # get variables first
        company_name = self.company_name_entry.get()
        company_enabled = self.company_is_enabled.get()
        api_url = self.api_url_entry.get()
        api_key = self.api_key_entry.get()
        
        # print variables
        print()
        print("Company Wizard Entries")
        print("======================")
        print(f"Company Name: {company_name}")
        print(f"Company Enabled: {company_enabled}")
        print(f"API URL: {api_url}")
        print(f"API Key: {api_key}")
        print()

    def run(self):
        self.mainwindow.mainloop()

    def close_window(self, event):
        self.mainwindow.destroy()


if __name__ == "__main__":
    # Change persistency_test to True to test pre-set values #
    persistency_test = False
    
    company_name = "My Sample Company" if persistency_test else ""
    company_enabled = False            if persistency_test else True
    api_url = "https://www.google.com" if persistency_test else ""
    api_key = "hu34hu9908yhxdf7g"      if persistency_test else ""
    
    # Create and open window
    app = CompanyWizardWindow(company_name=company_name,
                              company_enabled=company_enabled,
                              api_url=api_url,
                              api_key=api_key)
    app.run()
import tkinter as tk

def print_widget_config(widget: tk.Widget):
    attributes = widget.config()
    
    print("Widget Config")
    print("=============")
    
    for key in attributes:
        value = widget.cget(key)
        print(f"{key} = {value}")
    
    print()
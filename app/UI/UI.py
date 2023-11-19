import tkinter as tk

def display_text():
    input_text = entry.get()
    text_display.insert(tk.END, f"{input_text}\n")


# Create the main window
root = tk.Tk()
root.title("Text Display")
root.geometry("300x200")

# Create the text entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create the button widget
button = tk.Button(root, text="Display", command=display_text)
button.pack(pady=5)

# Create the text display widget
text_display = tk.Text(root, wrap=tk.WORD, height=5)
text_display.pack(pady=10, padx=10)

# Start the main loop
root.mainloop()

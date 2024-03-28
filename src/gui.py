import tkinter as tk
from tkinter import filedialog, messagebox
from main import convert


window = tk.Tk()

    # Create a label and entry for the input file
input_label = tk.Label(window, text="Enter the path of the document file:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

    # Create a label and entry for the output format
output_label = tk.Label(window, text="Enter the desired output format (pdf/docx/txt):")
output_label.pack() 
output_entry = tk.Entry(window)
output_entry.pack()

    # Create a button that will call the convert function when clicked
convert_button = tk.Button(window, text="Convert", command=lambda: convert(input_entry.get(), output_entry.get()))
convert_button.pack()

    # Start the Tkinter event loop
window.mainloop()
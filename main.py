from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog


def drag_file(event):
    file_path = event.data
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)


def browse_directory():
    directory_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, directory_path)


def convert():
    webp_path = file_entry.get().replace("\"", "").replace("\'", "")
    # remove any quotes from the input

    if not os.path.exists(webp_path):
        print("File " + webp_path + " does not exist")
        exit(1)

    image = Image.open(webp_path)
    image = image.convert('RGB')

    new_path = webp_path.replace(".webp", "." + option_var.get())
    print(new_path)
    image.save(new_path,option_var.get(), quality=100)

    filedialog.askopenfile(new_path)


# Create the main window
window = tk.Tk()
window.title("WEBPSUX")

# Create the file entry widget
file_label = tk.Label(window, text="Drag a file here:")
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(window, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
file_entry.bind("<Return>")

convert_button = tk.Button(window, text="Browse", command=browse_directory)
convert_button.grid(row=0, column=2, padx=10, pady=10)

# Create the radio buttons
option_var = tk.StringVar(value="jpeg")
option1_button = tk.Radiobutton(window, text="jpg", variable=option_var, value="jpeg")
option1_button.grid(row=1, column=0, padx=10, pady=10)
option2_button = tk.Radiobutton(window, text="png", variable=option_var, value="png")
option2_button.grid(row=2, column=0, padx=10, pady=10)

# Create the convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=3, column=1, padx=10, pady=10)

window.mainloop()

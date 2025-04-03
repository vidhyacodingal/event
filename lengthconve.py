import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")

# Create and place widgets
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Enter length in inches:").grid(row=0, column=0, padx=5, pady=5)
entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=5, pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert_to_cm)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()

import tkinter as tk

# Function to update the display
def on_click(button_text):
    current_text = display_var.get()
    display_var.set(current_text + button_text)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")

# Function to clear the display
def clear_display():
    display_var.set("")

# Create the main window
root = tk.Tk()
root.title("Custom Calculator")
root.geometry("350x500")
root.configure(bg="#2C3E50")  # Background color

# Create a StringVar to store the display value
display_var = tk.StringVar()

# Display Entry Field
display = tk.Entry(root, textvariable=display_var, font=("Arial", 24), bd=10, relief="ridge", justify="right", bg="#ECF0F1")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Button Layout (Match Your Figma Design)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create Buttons
for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 20), command=calculate, width=5, height=2, bg="#27AE60", fg="white")
    else:
        btn = tk.Button(root, text=text, font=("Arial", 20), command=lambda t=text: on_click(t), width=5, height=2, bg="#34495E", fg="white")
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear Button
clear_btn = tk.Button(root, text="C", font=("Arial", 20), command=clear_display, width=5, height=2, bg="#E74C3C", fg="white")
clear_btn.grid(row=5, column=0, columnspan=4, sticky="we", pady=10)

# Run the application
root.mainloop()


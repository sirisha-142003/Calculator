import tkinter as tk

# Function to handle button clicks
def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    elif text == "←":
        expression = expression[:-1]
        input_var.set(expression)
    else:
        expression += text
        input_var.set(expression)

# Initialize the main application
root = tk.Tk()
root.title("Alternative Layout Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Global variables
expression = ""
input_var = tk.StringVar()

# Display screen
display = tk.Entry(
    root, textvar=input_var, font=("Arial", 20), justify="right", bd=8, relief=tk.SUNKEN
)
display.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout (Alternative Design)
buttons = [
    ["C", "←", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "//", "="],
]

# Creating buttons using a grid layout with varied styling
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

for row_idx, row in enumerate(buttons):
    for col_idx, text in enumerate(row):
        # Different color schemes for different buttons
        if text in ("C", "←"):
            color = "#f77"  # Red for clear and backspace
        elif text in ("+", "-", "*", "/", "%", "//", "="):
            color = "#77f"  # Blue for operators
        else:
            color = "#ddd"  # Light gray for numbers and dot

        btn = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 18),
            relief=tk.RAISED,
            bd=3,
            bg=color,
            fg="black",
        )
        btn.grid(row=row_idx, column=col_idx, padx=5, pady=5, sticky="nsew")
        btn.bind("<Button-1>", click)

# Configure rows and columns to expand evenly
for i in range(len(buttons)):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):  # Four columns
    button_frame.columnconfigure(j, weight=1)

# Run the application
root.mainloop()

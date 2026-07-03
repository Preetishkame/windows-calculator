import tkinter as tk

# Function to add numbers and operators to the display
def click(value):
    entry_var.set(entry_var.get() + str(value))

# Function to clear the display
def clear():
    entry_var.set("")

# Function to calculate the result
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(True, True)

entry_var = tk.StringVar()

# Display
entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 24),
    justify="right",
    bd=10
)
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for button in row:
        if button == "=":
            cmd = calculate
        elif button == "C":
            cmd = clear
        else:
            cmd = lambda x=button: click(x)

        tk.Button(
            row_frame,
            text=button,
            font=("Arial", 18),
            command=cmd
        ).pack(side="left", expand=True, fill="both")

root.mainloop()

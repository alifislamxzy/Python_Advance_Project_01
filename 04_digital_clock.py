import tkinter as tk
from time import strftime

# Function to update the clock
def update_time():
    current_time = strftime("%H:%M:%S %p")  # Format: Hours:Minutes:Seconds AM/PM
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set up the clock display
label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
label.pack(anchor="center", pady=20)

# Start the clock
update_time()

# Run the application
root.mainloop()

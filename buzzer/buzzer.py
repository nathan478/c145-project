import tkinter as tk

def show_text():
    # Create a label widget to display the text
    label = tk.Label(window, text="user", font=("Helvetica", 24))
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    # Schedule the label to disappear after 1 second
    window.after(1000, label.destroy)

def on_left_click(event):
    show_text()
    # Flash the window
    window.attributes("-alpha", 0.3)
    window.after(100, lambda: window.attributes("-alpha", 1.0))

def on_right_click(event):
    # Reset the window and remove any displayed text
    window.attributes("-alpha", 1.0)
    for widget in window.winfo_children():
        widget.destroy()

# Create the main window
window = tk.Tk()
window.title("Flash and Text Example")
window.geometry("400x300")

# Bind left-click and right-click events to the window
window.bind("<Button-1>", on_left_click)
window.bind("<Button-3>", on_right_click)

# Start the main event loop
window.mainloop()
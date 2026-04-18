import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("600x200")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a1a")
        
        # Create main label for time
        self.time_label = tk.Label(
            self.root,
            font=("Helvetica", 80, "bold"),
            background="#1a1a1a",
            foreground="#00ff00"
        )
        self.time_label.pack(expand=True)
        
        # Create label for date
        self.date_label = tk.Label(
            self.root,
            font=("Helvetica", 20),
            background="#1a1a1a",
            foreground="#00ff00"
        )
        self.date_label.pack()
        
        # Update the clock
        self.update_time()
    
    def update_time(self):
        # Get current time and date
        time_string = strftime("%H:%M:%S")
        date_string = strftime("%A, %B %d, %Y")
        
        # Update labels
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        
        # Schedule next update after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()

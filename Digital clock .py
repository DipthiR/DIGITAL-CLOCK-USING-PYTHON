from tkinter import Label, Tk
import time

# Create app window
app = Tk()
app.title("🕒 Digital Clock")
app.geometry("420x200")
app.resizable(False, False)
app.configure(bg="#0f2027")  # Dark background

# Clock label
clock_label = Label(app, bg="#0f2027", fg="#00fff7",
                    font=("Helvetica", 60, "bold"))
clock_label.pack(pady=20)

# Date label
date_label = Label(app, bg="#0f2027", fg="#ffcc70",
                   font=("Helvetica", 20))
date_label.pack()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    
    clock_label.after(1000, update_time)

# Hover glow effect
def on_enter(e):
    clock_label.config(fg="#ff6ec4")  # Pink glow

def on_leave(e):
    clock_label.config(fg="#00fff7")  # Cyan glow

clock_label.bind("<Enter>", on_enter)
clock_label.bind("<Leave>", on_leave)

update_time()
app.mainloop()

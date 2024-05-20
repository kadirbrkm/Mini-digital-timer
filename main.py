from tkinter import Label, Tk
import time


app_window = Tk()
app_window.title("Digital Clock")
app_window.geometry("420x200")
app_window.resizable(False, False)
app_window.configure(bg="#f2e750")


text_font = ("Boulder", 68, 'bold')
date_font = ("Boulder", 20, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25


time_label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
time_label.grid(row=0, column=0, padx=5, pady=5)

date_label = Label(app_window, font=date_font, bg=background, fg=foreground)
date_label.grid(row=1, column=0, padx=5, pady=5)


app_window.grid_rowconfigure(0, weight=1)
app_window.grid_rowconfigure(1, weight=1)
app_window.grid_columnconfigure(0, weight=1)


def update_clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    time_label.after(200, update_clock)


update_clock()


app_window.mainloop()

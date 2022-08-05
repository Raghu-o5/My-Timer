from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
#https://matplotlib.org/stable/gallery/color/named_colors.html for different colors
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    #timer_text 00:00
    global reps
    reps = 0
# ---------------------------- STOP MECHANISM --------------------------------#
def stop_timer():
    window.after_cancel(timer)
    title_label.config(text="   Timer Stopped!"       )
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="  peww!! Tea time!   ", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text=" Play some Melodies! ", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="        Work         ", fg=GREEN)


'''1st repitition
    count_down(work_sec)
     2nd 4th rep 
     count-dwon(short_break_sec)
     7th or pomodoro technique which rep is long that has to be
     count_down = (long_break_sec)'''

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
'''import time
count = 5
while True:
    time.sleep(1)
    count-=1'''
def count_down(count):


    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    ''' 245 / 60 = 4 minutes
        245 % 60 = some_seconds'''
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Timer for me!")
window.config(padx=100, pady=50, bg=YELLOW)

'''def say_something(thing):
    print(thing)

window.after(1000, say_something, "Hello")
def say_something(a, b, c):
    print(a)
    print(b)
    print(c)

window.after(1000,say_something,3, 5, 8)'''



title_label = Label(text='Timer', fg=GREEN,bg=YELLOW, font=(FONT_NAME, 40))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
'''height and width of the image fixed can be setted'''
Pikachu = PhotoImage(file='download.png')

'''file name need to be specified with photoimagr class in tkinter '''
canvas.create_image(100, 112, image=Pikachu)


timer_text = canvas.create_text(60, 50, text='00:00', fill='skyblue', font=(FONT_NAME, 25, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
start_reset = Button(text="Reset", highlightthickness=0, command = reset_timer)
start_reset.grid(column=2, row=2)
stop = Button(text = "Stop", highlightthickness=0, command = stop_timer,bg="salmon")
stop.grid(column=0, row=3)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

'''User Interface is self doable'''
window.mainloop()


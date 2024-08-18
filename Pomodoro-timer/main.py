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
Font = ('Roboto',8)
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def Reset():
    global timer,reps
    global check_marks
    window.after_cancel(timer)
    canva.itemconfig(timer_text,text ="00:00")
    check_marks.config(text='')
    title_text.config(text='Timer',fg=GREEN)
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check_marks
    #Go to the bottom to see this code works
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
    if canva.itemcget(timer_text, 'text') == '00:00':
        reps += 1
        if reps % 8 == 0 :
            Countdown(LONG_BREAK_MIN*60)
            title_text.config(text='Break',fg=RED)
             #checkmark
            marks=''
            for _ in range(math.floor(reps/2)):
                marks+='✓'
            check_marks.config(text = marks)
        elif reps % 2 == 0:
            Countdown(SHORT_BREAK_MIN*60)
            title_text.config(text='Break',fg=PINK)
             #checkmark
            marks=''
            for _ in range(math.floor(reps/2)):
                marks+='✓'
            check_marks.config(text = marks)
        else :
            Countdown(WORK_MIN*60)
            title_text.config(text='Focus',fg=GREEN)

            
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def Countdown(count):
    global timer
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f'0{count_sec}'
    if count_min == 0:
        count_min = f'0{count_min}'
    
    canva.itemconfig(timer_text,text =f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,Countdown,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro-Timer')
window.config(padx=100, pady=50, bg=YELLOW)


canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomoto_image = PhotoImage(file='tomato.png')
canva.create_image(100, 112, image=tomoto_image)
timer_text = canva.create_text(100, 132, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canva.grid(column=2,row=2)


#title text
title_text = Label(text='Timer',font=(FONT_NAME,50),fg=GREEN,bg=YELLOW)
title_text.grid(column=2,row=1)
#start button
start_button = Button(text='Start',highlightthickness=0,command=start_timer)
start_button.grid(column=1,row=3)
#reset button
reset_button = Button(text='Reset',highlightthickness=0,command=Reset)
reset_button.grid(column=3,row=3)
#checkmarks
check_marks = Label(fg=GREEN,bg=YELLOW,font=('Roboto',12,'bold'))
check_marks.grid(column=2,row=4)

window.mainloop()

#------------------------From Stackoverflow------------------------#
# Assuming you mean your application windows when you say "my other windows", you can use the lift() method on a Toplevel or Tk:

# root.lift()
# If you want the window to stay above all other windows, use:

# root.attributes("-topmost", True)
# Where root is your Toplevel or Tk. Don't forget the - infront of "topmost"!

# To make it temporary, disable topmost right after:

# def raise_above_all(window):
#     window.attributes('-topmost', 1)
#     window.attributes('-topmost', 0)
# Just pass in the window you want to raise as a argument, and this should work.
from tkinter import Tk, Canvas, Label, Button, PhotoImage

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_canvas,text='00:00')
    Title_label.config(text='Timer')
    check.config(text='')
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1
    if reps%2:
        countdown(WORK_MIN*60)
        Title_label.config(text='WORK')
    elif reps==8:
        countdown(LONG_BREAK_MIN*60)
        Title_label.config(text='BREAK', fg=RED)
    else:
        countdown(SHORT_BREAK_MIN*60)
        Title_label.config(text='BREAK', fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min=count//60
    count_sec=count%60
    #itemconfig - это метод объекта Canvas в библиотеке tkinter, который позволяет изменять настройки элементов, созданных на холсте. В данном случае, метод itemconfig используется для изменения текста элемента timer_canvas на значение переменной count.
    canvas.itemconfig(timer_canvas,text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        #.after() - это метод объекта Tkinter, который позволяет запланировать выполнение функции через определенное количество миллисекунд. Первый аргумент - время задержки в миллисекундах, второй аргумент - функция, которую нужно выполнить после задержки.
        timer=window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark=""
        for i in range(reps//2):
            mark+='✓'
        check.config(text = mark)


        # ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_canvas = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


Title_label = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
Title_label.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0,command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=2)

window.mainloop()
import tkinter
from tkinter import *
import ttkbootstrap as tb
from texts import data

# Get data form texts.py
texts_dict = data
text_num = 0
character = 0
last_correct_count = 0
timer_1 = None
correct_char_sum = 0
correct_char = 0
cpm_count = 0
wpm_count = 0

def change_text():
    global text_num, last_correct_count, correct_char_sum, correct_char, wpm_count, cpm_count
    if len(entry_text.get("1.0", END)) == len(texts_dict[text_num]) + 1:
        text_num += 1
        display_text.config(text=texts_dict[text_num])
        correct_char_sum += correct_char
        entry_text.delete('1.0', END)
    char_index = str(entry_text.index("end-2c")).replace("1.", "")
    if texts_dict[text_num][int(char_index)] != entry_text.get("end-2c"):
        entry_text.tag_config(char_index, foreground="red")
        entry_text.tag_add(char_index, entry_text.index("end-2c"))
    else:
        entry_text.tag_delete(char_index)
        correct_char = correct_char_sum + len(entry_text.get("1.0", END)) - 1
        if correct_char > last_correct_count:
            wpm_count = (correct_char / 5)
            cpm_count = correct_char
            wpm.config(text=f"WPM: {wpm_count}")
            cpm.config(text=f"CPM: {cpm_count}")
            last_correct_count = len(entry_text.get("1.0", END)) - 1
    window.after(100, change_text)


def start():
    global wpm_count, cpm_count
    wpm_count = 0
    cpm_count = 0
    wpm.config(text=f"WPM: {wpm_count}")
    cpm.config(text=f"CPM: {cpm_count}")
    entry_text.config(state="normal")
    entry_text.delete('1.0', END)
    entry_text.focus_set()
    start_timer(60)


def start_timer(value):
    global timer_1
    timer.config(text=f"Time left: {value}")
    if value > 0:
        timer_1 = window.after(1000, start_timer, value - 1)
        str_button.config(state="disabled")
    else:
        window.after_cancel(timer_1)
        entry_text.config(state="disabled")
        str_button.config(state="normal")


# ---------------------------- UI SETUP ------------------------------- #

# Init window
window = tb.Window(themename='darkly')
window.title('Speed Typing')
window.geometry('600x320+650+300')
# Display text

display_text = tkinter.Label(text=f"Text to type:\n{texts_dict[text_num]}",
                             font=('Helvetica', 12),
                             anchor="center",
                             width=50,
                             wraplength=400)

display_text.grid(column=1,
                  row=1,
                  columnspan=2,
                  padx=20,
                  pady=20)

# Add timer
timer = tkinter.Label(text="Time left: 60",
                      font=('Helvetica', 12),
                      anchor="center", )
timer.grid(column=2,
           row=4,
           padx=20,
           pady=20)

# Add labels words/min and chars/min

wpm = tkinter.Label(text=f"WPM: {wpm_count}",
                    font=('Helvetica', 12),
                    anchor="center", )
wpm.grid(column=1,
         row=2,
         padx=20,
         pady=20)

cpm = tkinter.Label(text=f"CPM: {cpm_count}",
                    font=('Helvetica', 12),
                    anchor="center", )
cpm.grid(column=2,
         row=2,
         padx=20,
         pady=20)

# Add Text entry
entry_text = tkinter.Text(highlightbackground='#409700')
entry_text.config(fg='#40b400',
                  font=('Helvetica', 12),
                  width=50,
                  height=3,
                  insertwidth=3,
                  state="disabled")
entry_text.grid(column=1,
                row=3,
                padx=70,
                columnspan=2
                )

# Buttons
new_style = tb.Style()
new_style.configure('success.TButton',
                    font=('Helvetica', 12),
                    width=15)

str_button = tb.Button(text='Start', style='success.TButton', command=start)
str_button.grid(column=1,
                row=4,
                padx=38,
                pady=10
                )

change_text()
window.mainloop()

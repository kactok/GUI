import tkinter
from tkinter import *
import ttkbootstrap as tb
from texts import data

# Get data form texts.py
texts_dict = data
text_num = 0
character = 0


def change_text():
    global text_num
    if len(entry_text.get("1.0", END)) == len(texts_dict[text_num]) + 1:
        text_num += 1
        display_text.config(text=texts_dict[text_num])
        entry_text.delete('1.0', END)
    print(entry_text.get("end-2c"))
    print(texts_dict[text_num][int(float(entry_text.index("end-2c"))*10 % 10)])
    # if entry_text.get('1.0', END) != texts_dict[text_num][:len(entry_text.get('1.0', END)) - 1]:
    if texts_dict[text_num][int(float(entry_text.index("end-2c"))*10 % 10)] != entry_text.get("end-2c"):
        entry_text.tag_config("start", foreground="red")
        entry_text.tag_add("start", entry_text.index("end-2c"))
    else:
        print("Good")
        entry_text.tag_delete("start")
    window.after(100, change_text)


# ---------------------------- UI SETUP ------------------------------- #

# Init window
window = tb.Window(themename='darkly')
window.title('Speed Typing')
window.geometry('600x250+650+300')

# Display text

display_text = tkinter.Label(text=f"Text to type:\n{texts_dict[text_num]}",
                             font=('Helvetica', 12),
                             anchor="center",
                             width=50,
                             wraplength=400)

display_text.grid(column=1,
                  row=1,
                  padx=20,
                  pady=40)

# Add Text entry
entry_text = tkinter.Text(highlightbackground='#409700')
entry_text.config(fg='#40b400',
                  font=('Helvetica', 12),
                  width=50,
                  height=3)
entry_text.focus_set()
entry_text.grid(column=1,
                row=2,
                padx=70,
                )
change_text()
window.mainloop()

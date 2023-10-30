import os
import tkinter
from tkinter import filedialog
import ttkbootstrap as tb
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random


def open_img():
    global img
    """Display image"""
    # Path to the file
    folder_path = os.environ["FOLDER_PATH"]
    file_path = filedialog.askopenfilename(initialdir=folder_path, title='Select a file')
    # Open image
    with Image.open(file_path) as img:
        # Resize the image
        img = img.resize((1280, 720))
        new_img = ImageTk.PhotoImage(img)
    label1 = tkinter.Label(image=new_img)
    label1.image = new_img
    label1.grid(column=1,
                row=1,
                columnspan=3)
    add_watermark_btn.grid(column=3, row=2)
    text_to_add.grid(column=2, row=2)


def add_watermark():
    global img

    add_wm = ImageDraw.Draw(img)
    font = ImageFont.load_default(size=70)
    x, y = int(img.width / 2), int(img.height / 2)
    # add watermark
    add_wm.text((x, y),
                text=text_to_add.get(),
                font=font,
                fill='#FFF',
                anchor="ms",
                stroke_width=1,
                stroke_fill="#FFF")
    new_img = ImageTk.PhotoImage(img)
    label1 = tkinter.Label(image=new_img)
    label1.image = new_img
    label1.grid(column=1,
                row=1,
                columnspan=3)
    img.save(f"{os.environ['FOLDER_PATH']}/new_file{str(random.randint(0, 1000))}.jpg")


# Initialize window
root = tb.Window(themename='superhero')
root.title('Add a watermark')
root.geometry('1320x820+300+100')
root.config(padx=20,
            pady=20)

# ---------------------------- ADD BUTTONS ------------------------------- #
new_style = tb.Style()
new_style.configure('primary.TButton',
                    font=("Courier", 18),
                    width=15)
add_photo_btn = tb.Button(text="Open image",
                          style='primary.TButton',
                          command=open_img)
add_photo_btn.grid(column=1,
                   row=2)
add_watermark_btn = tb.Button(text="Add watermark",
                              style='primary.TButton',
                              command=add_watermark)
add_watermark_btn.grid(column=1, row=1, pady=20)

# ---------------------------- ADD Entry ------------------------------- #

text_to_add = tb.Entry(width=30, font=("Courier", 12))
text_to_add.grid(column=1, row=3, pady=20)

root.mainloop()

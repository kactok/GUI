import os
import tkinter
from tkinter import filedialog, PhotoImage, Canvas
import PIL
import ttkbootstrap as tb
from PIL import Image, ImageTk


def open_img():
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
                columnspan=2)
    add_watermark_btn.grid(column=2, row=2)


# Initialize window
root = tb.Window(themename='simplex')
root.title('Add a watermark')
root.geometry('1320x820+300+100')
root.config(padx=20,
            pady=20)

# ---------------------------- ADD BUTTONS ------------------------------- #
new_style = tb.Style()
new_style.configure('success.TButton',
                    font=("Courier", 18),
                    width=20)
add_photo_btn = tb.Button(text="Open image",
                          style='success.TButton',
                          command=open_img)
add_photo_btn.grid(column=1,
                   row=2)
add_watermark_btn = tb.Button(text="Add watermark",
                              style='success.TButton')
add_watermark_btn.grid(column=1, row=1, pady=20)
root.mainloop()

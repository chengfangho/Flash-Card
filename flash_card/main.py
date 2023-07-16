from tkinter import *
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
word = {}


def flip():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(img_canvas, image=img_card_back)
    canvas.itemconfig(spanish, text=word["English"], fill="white")

def next_word():
    global word
    global flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(words)
    canvas.itemconfig(title, text="Spanish", fill="black")
    canvas.itemconfig(img_canvas, image=img_card_front)
    canvas.itemconfig(spanish,text=word["Spanish"], fill="black")
    flip_timer = window.after(3000, flip)

def remove_word():
    words.remove(word)
    data = DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()



try:
    data = read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("data/spanish_words.csv")
finally:
    words = DataFrame.to_dict(data, orient="records")

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
img_card_front = PhotoImage(file="images/card_front.png")
img_card_back = PhotoImage(file="images/card_back.png")
img_canvas = canvas.create_image(400, 263, image=img_card_front)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic") )
spanish = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, height=95, width=95, highlightthickness=0, bd=0, command=remove_word)
button_right.grid(row=1, column=0)

img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, height=95, width=95, highlightthickness=0, bd=0, command=next_word)
button_wrong.grid(row=1, column=1)

next_word()
window.mainloop()


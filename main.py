from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/Hindi_words.csv")
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

# ----------------------------------------- function ----------------------------------------------
def next_card():
    global current_card, card_flip_timer
    window.after_cancel(card_flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi",fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"],fill="black")
    canvas.itemconfig(card_bg, image=front_image)
    card_flip_timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_bg,image=back_image)

def known_words():
    to_learn.remove(current_card)
    words = pd.DataFrame(to_learn)
    words.to_csv("data/words_to_learn.csv",index=False)
    next_card()

# -------------------------------------------- UI -------------------------------------------------

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

card_flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(window,width=800,height=530)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400,263,image=front_image)
card_title = canvas.create_text(400, 150, text="HINDI", font=("Courier", 30, "bold"), fill="black")
card_word = canvas.create_text(400, 263, text="krishna", font=("Courier", 30, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


wrong_image = PhotoImage(file="images/wrong.png")
wrong_mark =Button(window,image=wrong_image,command=next_card)
wrong_mark.grid(row=1,column=0)
right_image = PhotoImage(file="images/right.png")
right_mark =Button(window,image=right_image,command=known_words)
right_mark.grid(row=1,column=1)

next_card()

window.mainloop()





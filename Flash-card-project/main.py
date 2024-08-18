from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
#-------------------Creating a Card using the data file ------------------#
try:
    data = pandas.read_csv(r'data\words_to_learn.csv')
except (FileNotFoundError,pandas.errors.EmptyDataError):
    data = pandas.read_csv(r'data\french_words.csv')

data_dict = data.to_dict(orient='records')

def next_card():
    global current_card,timer
    window.after_cancel(timer)
    current_card = data_dict[random.randint(0,len(data_dict)-1)]
    random_french_word = current_card['French']
    canva.itemconfig(word,text=random_french_word,fill='black')
    canva.itemconfig(language_text,text='French',fill='black')
    canva.itemconfig(canva_image,image = question_image)
    #flipping card to show translation in english
    timer = window.after(3000,flip)
#------------------Removing Known words---------------#
def is_known():
    '''
    Removes the known word from the dictionary 
    '''
    global current_card
    data_dict.remove(current_card)
    df = pandas.DataFrame(data_dict)
    #the csv file is recreated each time the dictionary is altered.
    df.to_csv(r'data\words_to_learn.csv',index=False)
    next_card()

#--------------------Flip Card------------------#
def flip():
    global current_card
    canva.itemconfig(canva_image,image = card_back)
    canva.itemconfig(language_text,fill = 'white',text='English')
    canva.itemconfig(word,fill = 'white',text = current_card['English'])
    

#---------------------UI-----------------------#

window = Tk()
window.title('Flash-Cards')
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer = window.after(3000,flip)
#canvas
canva = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
question_image = PhotoImage(file=r'images\card_front.png')
card_back = PhotoImage(file=r'images\card_back.png')
canva_image = canva.create_image(400,263,image = question_image)
canva.grid(column=0,row=0,columnspan=2)
language_text = canva.create_text(400,150,text='French',font=('Arial',40,'italic'))
canva.place()
word = canva.create_text(400,263,font=('Arial',60,'bold'))
next_card()
canva.place()
#buttons
wrong_image = PhotoImage(file = r'images\wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

right_image = PhotoImage(file = r'images\right.png')
right_button = Button(image=right_image, highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)


window.mainloop()

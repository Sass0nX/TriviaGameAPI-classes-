import time
import json
import tkinter
from tkinter import *
import requests
import api
from tkinter import messagebox
from PIL import ImageTk, Image

class Window:
    def __init__(self, root, title):
        self.root = root
        self.title = title
        self.root = Tk()
        self.root.title(f'My {self.title} App')
        self.root.geometry('600x600')
        self.root.resizable(False, False)

class Buttons(Window):
    def __init__(self, root, title):
        super().__init__(root, title)
    def addbutton(self):
        self.vphoto = PhotoImage(file='V.png')
        self.xphoto = PhotoImage(file='X.png')
        self.myfalsebutt = Button(self.root, image=self.xphoto, command=false,width=200,height=200)
        self.myfalsebutt.place(x=60, y=350)
        self.mytruebutt = Button(self.root, image=self.vphoto, command=true,width=200,height=200)
        self.mytruebutt.place(x=310, y=350)
        self.root.mainloop()

class Labels(Buttons):
    def __init__(self, root, title):
        super().__init__(root, title)
        self.scoreresult = 0
        self.qnumber = 1
        self.canvas = tkinter.Canvas(self.root, bg='gray')
        self.canvas.pack()
        self.text = self.canvas.create_text(200, 70, width=270, text=f'Q{self.qnumber}.{api.getquestion()}', fill='black', font=15)
        self.score = Label(self.root, text=f'Score: {self.scoreresult}', font=20)
        self.score.place(x=100,y=0)

def set_new():
    myquizapp.canvas.itemconfig(myquizapp.text, fill='black')
    myquizapp.qnumber += 1
    myquizapp.canvas.itemconfig(myquizapp.text, text=f'Q{myquizapp.qnumber}.{api.getquestion()}')
    print(api.answer)
    print(myquizapp.qnumber)
    if myquizapp.qnumber == 11:
        exit = messagebox.askyesno('GAME OVER!!!', f'the game is over with score {myquizapp.scoreresult}, you want to play again?')
        if exit:
            myquizapp.qnumber = 1
            myquizapp.scoreresult = 0
            myquizapp.canvas.itemconfig(myquizapp.text, text=f'Q{myquizapp.qnumber}.{api.getquestion()}')
        else:
            myquizapp.root.destroy()

def false():
    if api.answer == 'False':
        myquizapp.canvas.itemconfig(myquizapp.text, fill='green')
        myquizapp.scoreresult += 1
        myquizapp.score.config(text=f'Score: {myquizapp.scoreresult}')
        myquizapp.canvas.after(1000, set_new)
    elif api.answer == 'True':
        myquizapp.canvas.itemconfig(myquizapp.text, fill='red')
        myquizapp.canvas.after(1000, set_new)

def true():
    if api.answer == 'True':
        myquizapp.canvas.itemconfig(myquizapp.text, fill='green')
        myquizapp.scoreresult += 1
        myquizapp.score.config(text=f'Score: {myquizapp.scoreresult}')
        myquizapp.canvas.after(1000, set_new)

    elif api.answer == 'False':
        myquizapp.canvas.itemconfig(myquizapp.text, fill='red')
        myquizapp.canvas.after(1000, set_new)


myquizapp = Labels('myquizapp', 'Quiz')
myquizapp.addbutton()






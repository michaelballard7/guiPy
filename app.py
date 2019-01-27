from tkinter import *

import pandas as pd

data = pd.DataFrame([1,2,3],[4,5,6], columns=["a"])

window = Tk()


def km_to_miles():
    print(data.head())
    miles = float(el_value.get())*1.6
    t1.insert(END,miles)


def load_player_data():
    data = pd.read_csv('')
    return data.head()


btn = Button(window,text="Bet Now",command=km_to_miles)
btn.grid(row=0, column=0)

el_value=StringVar()
el = Entry(window,textvariable=el_value)
el.grid(row=0,column=1)

t1 = Text(window,height=10,width= 20)
t1.grid(row=0,column=2)

window.mainloop()



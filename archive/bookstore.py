""" 
    A gui program to log all the books I own in an SQLLiteDB file

    Stores the following book information: Title, Author, Year, ISBN

    Users can: View all records, Search an Entry, Add an entry, Update Entry and Delete an enry

"""


from Tkinter import *

window = Tk()


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)


title_text = StringVar()
el = Entry(window, textvariable=title_text)
el.grid(row=0, column=1)

author_text = StringVar()
el2 = Entry(window, textvariable=author_text)
el2.grid(row=0, column=3)

year_text = StringVar()
el3 = Entry(window, textvariable=year_text)
el3.grid(row=1, column=1)

isbn_text = StringVar()
el4 = Entry(window, textvariable=isbn_text)
el4.grid(row=1, column=3)


list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

window.mainloop()

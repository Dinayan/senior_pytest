from tkinter import *
from tkinter.messagebox import showerror
import shelve
shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')
#print(('key',)+fieldnames)


def makeWidgets():
    global entries
    window = Tk()
    window.title("people shelve")
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',)+fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=FetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window


def FetchRecord():
    key = entries['key'].get()
    print('key:', key)
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def updateRecord():
    key = entries['key'].get()
    print(key)
    if key in db:
        record = db[key]
    else:
        from _senior_test_1.person import Person
        record = Person(name='?', age='?')
    for field in fieldnames:
        print('field', field)
        setattr(record, field, eval("entries[field].get()"))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()

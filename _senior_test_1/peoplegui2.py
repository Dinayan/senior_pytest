from tkinter import *
from tkinter.messagebox import showerror
import shelve


class people_gui2():

    def __init__(self, fieldnames, db):
        self.fieldnames = fieldnames
        self.db = db

    def makeWidgets(self):
        global entries
        window = Tk()
        window.title("people shelve")
        form = Frame(window)
        form.pack()
        entries = {}
        for (ix, label) in enumerate(('key',) + self.fieldnames):
            lab = Label(form, text=label)
            ent = Entry(form)
            lab.grid(row=ix, column=0)
            ent.grid(row=ix, column=1)
            entries[label] = ent
        Button(window, text='Fetch', command=self.FetchRecord).pack(side=LEFT)
        Button(window, text='Update', command=self.updateRecord).pack(side=LEFT)
        Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
        return window

    def FetchRecord(self):
        key = entries['key'].get()
        print('key:', key)
        try:
            record = self.db[key]
        except:
            showerror(title='Error', message='No such key!')
        else:
            for field in self.fieldnames:
                entries[field].delete(0, END)
                entries[field].insert(0, repr(getattr(record, field)))

    def updateRecord(self):
        key = entries['key'].get()
        print(key)
        if key in self.db:
            record = self.db[key]
        else:
            from _senior_test_1.person import Person
            record = Person(name='?', age='?')
        for field in self.fieldnames:
            print('field', field)
            setattr(record, field, eval("entries[field].get()"))
        self.db[key] = record


if __name__ == '__main__':
    db = shelve.open('class-shelve')
    fieldnames = ('name', 'age', 'job', 'pay')
    test_peoplegui = people_gui2(fieldnames, db)
    window = test_peoplegui.makeWidgets()
    window.mainloop()
    db.close()

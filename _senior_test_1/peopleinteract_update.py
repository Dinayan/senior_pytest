import shelve
from _senior_test_1.person import Person
fieldname = ('name', 'age', 'job', 'pay')
maxfield = max(len(f) for f in fieldname)
print(maxfield)
db = shelve.open('class-shelve')
while True:
    key = input('\nKey? => ')
    if not key:break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldname:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
            newtext1 = getattr(record,field)
            print(newtext1)
    db[key] = record
db.close()


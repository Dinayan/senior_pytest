#test range()用法
Name, ID, pay = range(3)
print('Name:', Name)
print('ID:', ID)
print('PAY:', pay)

#map()
l2 = map(lambda x, y: x**y, [1, 2, 3], [1, 2, 3])
for i in l2:
    print('12:', i)

#index
l3 = map(lambda x, y: (x**y, x+y), [1, 2, 3], [1, 2, 3])
for i in l3:
    print(i)
num = [45, 67, 464]
print('num.index(45):', num.index(45))

#zip
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
zip1 = list(zip(names, values))
print('zip1:', zip1)
people1 = [dict(zip1)]

fields = ['name', 'age', 'job', 'pay']
record = dict.fromkeys(fields, '?')
print('record:', record)

map1 = list(map((lambda x: x['name']), people1))
print('map1:', map1)


bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
people = [bob, sue]
rec1 = [(rec['age']**2 if rec['age'] >= 45 else rec['age']) for rec in people]
print('rec1:', rec1)
rec2 = [(rec['age']**2 if rec['age'] >= 45 else rec['age']) for rec in people]
#print('rec2.__next:', rec2.__next__())

rec3 = (rec['name'] for rec in people if rec['name'] >= 45)
print('rec3:', rec3)
#next(rec3)
print('hello')
print('Dina')
key=input("please:")
print(key)
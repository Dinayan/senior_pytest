import shelve
from _senior_test_1.person import Person
from _senior_test_1.manager import Manage
db = shelve.open('class-shelve')
bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manage('Tom Doe', 50, 50000)
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close()

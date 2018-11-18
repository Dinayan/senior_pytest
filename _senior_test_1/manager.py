from _senior_test_1.person import Person


class Manage(Person):
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = 'manager'

    def giveRise(self, percent):
        self.pay *= (1+percent+0.10)


if __name__ == '__main__':
    # bob = Person('Bob Smith', 42, 10000, 'software')
    # sue = Person('Sue Jones', 45, 20000, 'hardware')
    # tom = Manage(name='Tom Doe', age=50, pay=30000)
    # people = [bob, sue, tom]
    # for obj in people:
    #     obj.giveRise(0.10)
    # for obj in people:
    #     print(obj.lastName(), '=>', obj.pay)
    # Manage.giveRise(tom, 0.1)
    # print(tom.pay)
    tom = Manage(name='Tom Jones', age=50, pay=50000)
    print(tom.job)


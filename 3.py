class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self.income.values())


p = Position('Arkadiy', 'Petrovich', 'Employee', 5000, 1000)
print('income: ', p.get_total_income())
print('fullname: ', p.get_full_name())

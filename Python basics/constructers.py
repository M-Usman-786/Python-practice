class Employee:
    no_of_subject = 12
    def __init__(self, _name, _age, _study):
        self.name = _name
        self.age = _age
        self.study = _study
    def print_details(self):
        print(f"Name is {self.name} age is {self.age} study is {self.study}")


usman = Employee("Usman", 21, "Bechlares")
Ali = Employee("Ali", 22, "Fsc")

"""Ali = Employee()

usman.name = "Usman"
usman.age = 21
usman.study = "Bechulars"

Ali.name = "Ali"
Ali.age = 22
Ali.study = "Fsc"
"""
usman.print_details()
Ali.print_details()
usman.name = "Huzaifa"
usman.print_details()

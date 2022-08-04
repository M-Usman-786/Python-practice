class Employee:
    no_of_subject = 12


usman = Employee()
Ali = Employee()

usman.name = "Usman"
usman.age = 21
usman.study = "Bechulars"

Ali.name = "Ali"
Ali.age = 22

print(usman.__dict__)
print(usman.no_of_subject)
usman.no_of_subject = 16
print(usman.no_of_subject)
print(usman.__dict__)
print(Ali.__dict__)
print(Employee.__dict__)
Employee.no_of_subject = 15
print(Employee.__dict__)
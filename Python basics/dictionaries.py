customer = {
    "Name" : "Jhon Smith",
    "Age" : 19,
    "Is_verified" : True
}
print(customer["Name"])
print(customer.get("Age"))

customer["Name"] = "Jack Sparrow"
print(customer["Name"])

customer["Birthdate"] = "Jan 01 1999"
print(customer["Birthdate"])
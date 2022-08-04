phone = input("phone: ")

digit_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)
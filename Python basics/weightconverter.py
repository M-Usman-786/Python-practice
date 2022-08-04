weight = int(input("Enter the weight: "))
unit = input("(L)bs or (k)g: ")
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"The value is {converted} in kilos")
elif unit.upper() == 'K':
    converted = weight / 0.45
    print(f"The value is {converted} in Lbs")




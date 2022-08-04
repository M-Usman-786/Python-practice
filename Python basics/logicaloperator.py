#logical operator
 
has_good_income = True
has_good_credit = False

if has_good_income and has_good_credit:
    print("both are true")
if has_good_credit or has_good_income:
    print("1  one or more is true")
if has_good_credit or not(has_good_income):
    print("2  one or more is true")
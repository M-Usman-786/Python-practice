#if else




Price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * Price
else:
    down_payment = 0.2 * Price

print(f"Down payment is : ${down_payment}")


def max_number(number):
    maximum = number[0]
    for i in number:
        if i > maximum:
            maximum = i
    return maximum

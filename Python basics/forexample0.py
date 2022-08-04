
number = [5, 2, 5, 2, 2]
for x_count in number:
    print('x' * x_count)

#similarly
for x_count in number:
    output = 'x'
    for count in range(x_count):
        output += 'x'
    print(output)
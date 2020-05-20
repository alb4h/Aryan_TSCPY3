def print_multiples(n):
    for i in range(1, 7):
        print(n * i, end=" ")
    print()

def print_mult_table():
    for i in range(1, 7):
        print_multiples(i)

print_mult_table()
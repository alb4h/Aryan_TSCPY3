def sum_of_square(xs):
    count = 0
    for i in xs:
        i = i ** 2
        count += i
    return count

print(sum_of_square([1, 2, 3]))
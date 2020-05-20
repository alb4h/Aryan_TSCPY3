def mirror(fruit):
    sz = len(fruit)
    count = 0
    for i in fruit:
        count += 1
        fruit = fruit + fruit[sz-count]
    return fruit


print(mirror("nice"))

prefixes = "JKLMNOPQ"
suffix = "ack"
u = "u"

for letter in prefixes:
    if letter == prefixes[5] or letter == prefixes[7]:
        print(letter + u + suffix)
    else:
        print(letter + suffix)
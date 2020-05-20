def paragraph():
    count = 0
    count2 = 0
    paragraph = ''' this is a practice test. the word healed has two e's in it. Yea'''
    punctuation = """!()-[]{};:'"\,<>./@#$%^&*~"""

    for x in paragraph.lower():
        if x in punctuation:
            newstr = paragraph.replace(x, "")
    xs = paragraph.split()
    e = "e"
    for i in xs:
        length = len(xs)
        for a in i:
            if a == e:
                count2 += 1
                if count2 > 1:
                    count2 = 1
                    count = count + count2
    percent = length / count * 100
    print('Your text contains', length, 'words, of which', count, '(', percent, '%) contain an "e"')
paragraph()

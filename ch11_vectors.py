import sys
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    # test(add_vectors([1, 1], [1, 1]) == [2, 2])
    # test(add_vectors([1, 2], [1, 4]) == [2, 6])
    # test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
    # test(scalar_mult(5, [1, 2]) == [5, 10])
    # test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
    # test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
    # test(dot_product_2([1, 1], [1, 1]) == 2)
    # test(dot_product_2([1, 2], [1, 4]) == 9)
    # test(dot_product_2([1, 2, 1], [1, 4, 3]) == 12)
    # test(replace("Mississippi", "i", "I") == "MIssIssIppI")
    #
    # s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    # test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")
    # test(replace(s, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

# def add_vectors(u, v):
#     w = []
#     for i in range(len(u)):
#         sum = u[i] + v[i]
#         w.append(sum)
#     return w
#
# def scalar_mult(s, v):
#     w = []
#     for i in range(len(v)):
#         product = v[i] * s
#         w.append(product)
#     return w
#
#
# def dot_product_2(u, v):
#     sum = 0
#     for i in range(len(u)):
#         product = u[i] * v[i]
#         sum += product
#     return sum
#
# def replace(s, old, new):
#     s = s.replace(old, new)
#     return s


# test_suite()


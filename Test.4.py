# def multiplication(a, b):
#     i = (a * b)
#     return i
#
#
# a = 7
# b = 9
#
# for v in range(10):
#     print(multiplication(a, b))
#     a = a + 1
#     b = b + 1

# a = [1, 2, 3, 4, 5, 6, 7, 7]
# for i in a:
#     print(i)


def printList(a):
    for i in a:
        print(i)


a = [1, 2, 3, 4, 5, 6, 7, 7]

print(printList(a))


def convert2List(l, m, k):
    return [l, m, k]


d = 2
s = 40
u = 32

x=convert2List(d, s, u)
printList(x)
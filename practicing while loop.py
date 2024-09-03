# i = 0
# while (i < 50 + 1):
#     print(i)
#     i = i + 1
#
# n = int(input("enter a number:"))
# while (n <= 38):
#     n = int(input("enter a number:"))
#     print(n)
#
# q = 10
# while (q > 0):
#     print(q)
#     q = q - 1
# else:
#     print("i am in else")
#
# while True:
#     number = int(input("Enter a number greater than 10: "))
#
#     if number > 10:
#         print("Valid number: {number}")
#         break
#     else:
#         print("Number is not greater than 10. Please try again.")
#
# m = 0
# while True:
#     print(m)
#     m = m + 1
#     if (m % 100 == 0):
#         break
#

# def calculategmean(a, b):
#     mean = (a * l) % (a + l)
#     print(mean)


# def isgreater(a, b):
#     if (a > b):
#         print("a is greater")
#     else:
#         print("b is greater or equal")
#
#
# a = 6
# l = 7
# calculategmean(a, l)
# isgreater(a, l)
# # gmean = (a * l) % (a + l)
# # print(gmean)
# c = 88
# p = 33
# calculategmean(c, p)
# isgreater(c, p)


# def average (a, b):
#     print("the average is ", (a+b)/2)
#
#
#
# average(b=65,a=34)


# k = 99


# def hi(a, b):
#     i = (a * b + a + b)
#     print(i)
#     print(k)
#
#
# d = 77
# j = 88
# hi(d, j)


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("the average is ", sum / len(numbers))
    return sum / len(numbers)


s = average(88, 208, 77)
print(s)

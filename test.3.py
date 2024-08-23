# 1 odd
# 2 even
# 3 odd
# 4 even
# 5 odd
# 6 odd
# 7 odd
# 8 odd
# 9 odd
# loop 50 tak chalana ha


for i in range(50 + 1):
    if i == 0:
        print(i, "neither")
    elif i & 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")
        

# x = input("enter the name of the animal:")
# match x:
#     case "elephant" | "cat" | "dog":
#         print("mammals")
#     case "sparrow" | "eagle" | "penguin":
#         print("birds")
#     case "snake" | "lizard" | "crocodile":
#         print("reptiles")
#     case _:
#         print("unknown")
# 3 sides: "Triangle"
# 4 sides: "Quadrilateral"
# 5 sides: "Pentagon"
# 6 sides: "Hexagon"
# 7 sides: "Heptagon"
# 8 sides: "Octagon"
# Other: Any number of sides that does not match the above categories should return "Unknown Polygon".
#
z = int(input("enter a num of sides:"))
match z:
    case 3:
        print("triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case 6:
        print("hexagon")
    case 7:
        print("heptagon")
    case 8:
        print("octagon")
    case _:
        print("unknown")

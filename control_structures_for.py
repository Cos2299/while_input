big_ship = int(input("Enter the coordinate of the big ship: "))
for x in range(1, 11):
    if x == big_ship:
        print("W", end="")
    elif x == 5:
        print("B", end="")
    elif x == 10:
        print("~~WWW~~" ,end="")
    else:
        print("~", end="")
print()

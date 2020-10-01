side_a = int(input("Enter measurement: "))
side_b = int(input("Enter measurement: "))
side_c = int(input("Enter measurement: "))
print("a sq is ", (side_a**2))
print("b sq is ", (side_b**2))
print("c sq is ", (side_c**2))
print("a2 + b2 is ", (side_a**2)+(side_b**2))
if side_a**2 + side_b**2 == side_c**2:
    print("triangle is a right angle triangle")
else:
    print("triangle is not a right angle triange")
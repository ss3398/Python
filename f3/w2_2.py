"""
    Salma Ali
    ENTD 200 D004 Spr 20
    Edeki, Charles
    Week  6
    July 7, 2020
"""
Choice = "y"
while(Choice == "y"):
    Gas = float(input("Enter the gas quantity in gallons: "))
    Miles = float(input("Enter the number of miles: "))
    MPG = Miles / Gas
    print("MPG is : %.2f"%MPG)
    Choice = input("Do you want to calculate again? (y/n) ")
print("Thanks for taking your time.")

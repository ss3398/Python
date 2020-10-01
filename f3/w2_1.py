"""
    Salma Ali
    ENTD 200 D004 Spr 20
    Edeki, Charles
    Week  6
    July 7, 2020
"""
Choice = "y"
while(Choice == "y"):
    HourlyRate = int(input("Enter Rate per hour: "))
    HoursWorked = int(input("Enter hours worked: "))
    AmountPaid = HourlyRate*HoursWorked
    print("The amount paid is: ",AmountPaid)
    Choice = input("Do you want to calculate again? (y/n) ")
print("Thanks for taking your time.")
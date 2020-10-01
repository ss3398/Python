first = int(input("Enter the first number:"))

second = int(input("Enter the second number:"))

third = int(input("Enter the third number:"))

fourth = int(input("Enter the fourth number:"))

fifth = int(input("Enter the fifth number:"))

interest = 0.069

subtotal = first + second + third + fourth + fifth

balance = subtotal + interest

print("balance is", subtotal * interest)

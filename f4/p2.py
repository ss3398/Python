Item_One = float(input("Enter the purchase amount for Item #1: "))
Item_Two = float(input("Enter the purchase amount for Item #2: "))
Item_Three = float(input("Enter the purchase amount for Item #3: "))
Sub_Total = Item_One + Item_Two + Item_Three
State_Tax = 0.09 * Sub_Total
Total_With_Tax = Sub_Total + State_Tax
Discount_One = 0.05
Discount_Two = 0.03
Discount_given = 0.0

if Total_With_Tax > 5000:
    Discount_given = Discount_One * Total_With_Tax
elif Total_With_Tax > 3000:
    Discount_given = Discount_Two * Total_With_Tax


Discounted_total = Total_With_Tax - Discount_given

print("Item 1: ",Item_One)
print("Item 2: ",Item_Two)
print("Item 3: ",Item_Three)
print("Subtotal ",Sub_Total)
print("Total with tax ",Total_With_Tax)
print("Discount: ",Discount_given)
print("Total after discount: ",Discounted_total)




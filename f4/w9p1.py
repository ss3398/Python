def my_total_cost(paint_amt, price_per_gallon, labor_hours, labor_per_hour):
    return ((paint_amt*price_per_gallon) + (labor_hours*labor_per_hour))

# Declare all variables and assign value. Two are provided by the user.
# The others are assigned directly or using a formula.
v_wall_space = float(input("Enter the wall space in square feet: "))
v_price_per_gallon = float(input("Enter the price per gallon for the paint: "))
v_paint_amt = v_wall_space/112.0
v_labor_hours = (v_wall_space/112.0)*8.0
v_labor_per_hour = 35.0
# Call the function to get the total cost
v_tot_cost = my_total_cost(v_paint_amt, v_price_per_gallon, v_labor_hours, v_labor_per_hour)
print("Gallons of paint: %.2f" % v_paint_amt)
print("Hours of labor: %.2f" % v_labor_hours)
print("Paint charges: $ %.2f" % (v_paint_amt*v_price_per_gallon))
print("Labor charges: $ %.2f" % (v_labor_hours*v_labor_per_hour))
print("Total cost is: $ %.2f" % v_tot_cost)


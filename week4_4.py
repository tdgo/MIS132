# MIS132 - April 16
# Paint Job Estimator

area = float(input("Enter the square feet of wall space to be painted: "))
paint_price = float(input("Enter the price of the paint per gallon: "))

def calculate(area, paint_price):
    paint_cost = area / 112 * paint_price
    labor_charges = area / 112 * 8 * 35
    print("The number of gallons of paint required",format(area/112))
    print("The hours of labor required", format(area/112*8))
    print(f"The cost of the paint {paint_cost}")
    print(f"The labor charges {labor_charges}")
    print(f"The total cost of the paint job {paint_cost + labor_charges}")

calculate(area, paint_price)
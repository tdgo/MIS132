# MIS132 - April 16
# Future Value

present_value = float(input("Enter the amount of money in your account: "))
monthly_interest_rate = float(input("Enter the monthly interest rate: "))
monthly_interest_rate /= 100
time = int(input("Enter the number of the months that the money will be left in the account: "))

def calculate(present_value, monthly_interest_rate, time):
    future_value = present_value * ((1+monthly_interest_rate) ** time)
    print(f"The account's future value is {future_value}")

calculate(present_value, monthly_interest_rate, time)
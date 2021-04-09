# MIS 132 - April 9

# Week1: fundamentals, functions, conditionals
# Week2: iterations, strings, tuples
# Week3: lists, dictionaries, files

# Data types: strings, integers, floats, tuples, lists, dictionaries, booleans
my_string = "This is a string!"
my_num = 2
my_float = 2.2

my_tuple = (1,2,3,4,5,6)
my_list = ["a","b","c","d"]
operating_systems = {"Apple":{"desktop":"macos", "mobile":"ios"}, "Microsoft":"Windows", "Google":{"Desktop":"Chromeos", "Mobile":"Android"}}
#print(operating_systems)

user_list = {1:{"user_id":1, "user_name":"a", "email":"a(at)boun.edu.tr"},
             2:{"user_id":2, "user_name":"b", "email":"b(at)boun.edu.tr"}}

#print(user_list.keys())
#print(user_list.values())


# Conditionals
# if, elif, else


# Overtime payment calculator function
def payment_calc():
    """
    This function calculates the overtime payment and print
    gross payment.
    :return:
    """
    base_hours = 40
    overtime_multiplier = 1.5

    hours = " "
    pay_rate = " "

    while hours.isnumeric() == False:
        hours = input("Please enter the worked hours by the employee: ")
    hours = float(hours)

    while pay_rate.isnumeric() == False:
        pay_rate = input("Please enter the pay rate: ")
    pay_rate = float(pay_rate)

    if hours > base_hours:
        overtime_hours = hours - base_hours
        overtime_pay = overtime_hours * overtime_multiplier * pay_rate
        gross_pay = (base_hours * pay_rate) + overtime_pay
    elif hours < base_hours:
        gross_pay = hours * pay_rate
        print("The employee has workes less than BASE HOURS!")
    else:
        gross_pay = hours * pay_rate

    print(f"The gross pay is {gross_pay}")

#payment_calc()

def total_payment_calc():
    """
    The function asks for number of employees, then calculates the payments for the employees.
    :return:
    """
    num_employees = " "

    while num_employees.isnumeric() == False:
        num_employees = input("Plese enter the number of employees: ")
    num_employees = int(num_employees)

    hours = [0] * num_employees

    for i in range(num_employees):
        employee_hours = " "
        while employee_hours.isnumeric() == False:
            employee_hours = input("Enter the hours worked by the employee {}: ".format(i+1))
        hours[i] = float(employee_hours)

    pay_rate = float(input("Enter the pay rate: "))


    total_pay = 0
    for i in range(num_employees):
        gross_pay = hours[i] * pay_rate
        total_pay = total_pay + gross_pay
        print(f"The gross pay for the employee is {gross_pay}")

    print(f"The total payment you need to make is {total_pay}")

#total_payment_calc()


my_string = "BOUN"

#print(my_string * 3)

my_list = [1,2,3,4,5]
another_list = [10,20]
# Nested iterations
for item in my_list:
    for i in another_list:
        #print(item*i)
        pass

#print(len(my_string))

university = "Boğaziçi University"
#print(university[0:8])

letters = "abcdefghjkl"
#print(letters[::2])

# Files
f = open("file_example1.txt")
lines = f.readlines()
#print(lines)

new_lines = []
for item in lines:
    changed_line = item.strip("\n")
    new_lines.append(changed_line)

#print(new_lines)

fw = open("file_example1.txt", "w")
for item in new_lines:
    fw.write(item+"\nMIS132 \n")
fw.close()

# Functions

def greet(name):
    print(f"Hello {name}")

greet("MIS132")

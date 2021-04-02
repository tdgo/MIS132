# MIS 132 - April 2

# Iterations
# Strings
# Tuples

# While Loops
i = 1
while i < 5:
    #print(i)
    i += 1

i = 1
while i < 5:
    #print(i)
    if i == 2:
        break
    i += 1

while i < 5:
    i += 1
    if i == 3:
        continue
    #print(i)

# For Loops
mytuple = (1, 2, 3, 4, 5)

for item in mytuple:
    #print(item)
    #print(item * 2)
    pass

my_articles = ("First Article", "Second Article", "Some News")

for item in my_articles:
    pass

#print(my_articles[1])

# Strings
my_string = "This is a string!"

new_string = my_string.lower()
#print(new_string)
new_string = new_string.capitalize()
#print(new_string)
# print(new_string.isnumeric())

numerical_string = "2131"
#print(numerical_string.isnumeric())

my_string = "1"
while my_string.isnumeric() == False:
    # my_string = input("Please enter a number: ")
    pass

my_string = "This is a new string!"
#print(my_string[0])
#print(my_string[4:])
#print(my_string[:4])
#print(my_string[0:6])

my_string = "abcdefgh"
#print(my_string[0::4])

for item in "mystring":
    #print(item)
    pass

#print(len(my_string))

fruit = "banana"
print(fruit.find("ba"))

"""
registered_email = "blabla@boun.edu.tr"
email_input = ""
while email_input != registered_email:
    email_input = input("Please enter your email: ")
print(email_input)
"""

# Tuples
my_tuple = ("String values",1231213,False, ("I am inside a tuple!",2,3))
print(my_tuple[3][0])

#users = (("Blabla", "Aaaa","blabal@boun.edu.tr"),("Bla", "bla@boun.edu.tr"))
#print(users[0][0][0] + users[0][1][0])

#Tuples are immutable!
#my_tuple[0] = "We can't assign again!"



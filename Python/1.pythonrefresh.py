# @Date:   2019-01-01T11:10:47+01:00
# @Last modified time: 2019-01-01T12:10:46+01:00

# f5 to run
print(" _______________________VARIABLES______________________\n\n")

age = 20

name = "Ivan"

print("Hello my name is {} and my age is {}\n\n".format(name, age))


print(" _______________________CONDITION______________________\n\n")

boolean = False

if age > 18:
    print("You're older than 18")
    boolean = True
else:
    print("You're too young !")

if boolean:
    print("The boolean is True")

print("\n")


print(" _______________________FUNCTION______________________\n\n")

def hello(theString):
    print("Starting with " + theString)

hello("a string made by hand")


print("\n")

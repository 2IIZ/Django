# @Date:   2019-01-01T11:10:47+01:00
# @Last modified time: 2019-01-03T09:57:23+01:00

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


print(" _______________________LISTS______________________\n\n")

dogNames = ["Jax", "Cro", "Iv", "Squalo"]

#print list
print(dogNames)

#add one item
dogNames.insert(0, "AddedTo0")
print(dogNames)

#show one item
print(dogNames[3])

#del one item
del(dogNames[4])
print(dogNames)

#length of list
print(len(dogNames))

print("\n")

print(" _______________________LOOPS______________________\n\n")

for dog in dogNames:
	print(dog)

print("\n")

for x in range(0, 11):
	print(x)

print("\n")

bool = True
while bool == True:
	print(bool)
	bool = False

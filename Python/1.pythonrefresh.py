# @Date:   2019-01-01T11:10:47+01:00
# @Last modified time: 2019-01-03T10:36:42+01:00

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

#go through 0 to 10
for x in range(0, 11):
	print(x)

print("\n")

bool = True
#verify if it's true then print true
while bool == True:
	print(bool)
	bool = False


print(" _______________________DICTIONARIES______________________\n\n")

goats = {"Fido":8, "Camop":10, "Thor":4}

#print the age of Fido !
print(goats["Fido"])

#kill one goat
del(goats["Camop"])

#new born
goats["Pedro"] = 0

#print all goats
print(goats)

print("\n")

print(" _______________________CLASS______________________\n\n")

class Goat:
	goatInfo = "Goat are masters"

	#self is added to show the inner content (python's practice)
	def __init__(self, name, age, furcolor):
		self.name = name
		self.age = age
		self.furcolor = furcolor

	# bleat = bark for a goat
	def bleat(self):
		print("BEEEEEE")

mygoat = Goat("Jax", "2", "Red")
mygoat.bleat()


print(mygoat.name)
print(Goat.goatInfo)

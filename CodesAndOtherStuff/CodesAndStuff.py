# strings
# data that falls within " " marks

# concatenation
# put 2 or more strings together

firstname = "Emily"
lastname = "Rojas"

print(firstname + " " + lastname)

print("Emily Rojas")

# repitition
# repition operator:

print("hip "*2 + "Hooray!")

def rowYourBoat():
    print("Row, "*3 + 'your boat')
    print("Gently down the stream.")
    print("Merrily, "*4)
    print("life is but a dream.")

rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)
middleIndex = len(name) // 2
print(middleIndex)
print(name[middleIndex])

print(name[-1])

for i in range(len(name)):
    print(name[i])

# Slicing and Dicing
# slicing operator:
# makes Substrings.

print(name[0:3])
print(name[:5])
print(name[6:9])
print(name[6:])

for i in range(1, len(name)+1):
    print(name[0:i])

# search inside of strings

print("biv" in name)
print("V" not in name)

if "Y" in name:
    print("The letter Y is in name")
else:
    print("The letter Y is not in name.")


# String Methods to investigate:
 # Method        Use Example         Explanation
    # center        aStr.center(w)
    # ljust         aStr.ljust(w)
    # rjust         aStr.rjust(w)
    # upper         aStr.upper()
    # lower         aStr.lower()
    # index         aStr.index(item)
    # rindex        aStr.rindex(item)
    # find          aStr.find(item)
    # rfind         aStr.rfind(item)
    # replace       aStr.replace(old, new)

    # Be sure to include multiple examples of all of them in use

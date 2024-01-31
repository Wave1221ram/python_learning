#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# LISTS

fruits = ["apple", "orange", "banana", "coconut"]
# each value in a collection is also known as an element
print(fruits)
print(fruits[0:1:1])

for fruit in fruits:
    print(fruit)

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits[0] = "pineapple"

fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
fruits.index("apple")
fruits.count("banana")


# SET
fruits = {"apple", "orange", "banana", "coconut"}

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits.add("pineapple")
fruits.remove("apple")
fruits.pop()
fruits.clear()

fruits.add("coconuts")

# TUPLES
fruits = ("apple", "orange", "banana", "coconut")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple" in fruits)

fruits.index("apple")
fruits.count("coconut")






# ---------------------------------------
# New Keywords:
# dir()
# help()
# len()
# in

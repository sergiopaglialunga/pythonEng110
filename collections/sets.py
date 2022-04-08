# Sets

utensils = {"fork", "knife", "spoon", "spatula"}
print(utensils, type(utensils))

# sets are unordered, we can't access the elements
# an unique collection
utensils.add("spoon")
print(utensils)

replist = [1, 1, 2, 2, 3]
print(list(set(replist)))

x = frozenset([1, 2, 4, 6])
print(x, type(x))
# Dictionaries - a built-in data type that stores data in a
# collection of key-value pairs, muttable , keys are immutable  but any data type
# ues of curly {} braces contain keys and values separated by :
# years = { "Layla" - key : 1974 - value, "Ackeem" - key : 1997 - value}

# .get method() - returns the value of the selected key
stuff = {"food" : 15, "energy" : 100, "enemies" : 3}

print(stuff.get("food"))
"""
# .items method() - Takes the name of the dictionary and outputs the view of the key : value
# pair. you can leave the parathesis empty because items accepts the dictionary.
print(stuff.items())

# .keys method() -  Returns a view of all the keys in the dictionary,
# the parathesis can remain empty because accepts the whole dictionary as an arguement
print(stuff.keys())

# pop.item() - Allows the removal of the last itme in the dictionary, no argu is needed
print(stuff.popitem())
print(stuff)

# .setdefault() - Allows seeing what the value is of a key tha is in the dictionary
# and allows us to set a default value when a key is not in the dictionary and
# add the value

print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)"""

# .update() - is used to merge key-value pairs from one dictionary or iterable into
# another

#new dictionary and .update method
new_items = {"rocks" : 4, "arrows" : 18}
stuff.update(new_items)
print(stuff)

# updating the new_items dictionary values
new_items = {"rocks": 2, "arrows":5}
stuff.update(new_items)
print(stuff)

# add a new dictionary and update
up_new = {"food": 3, "webs":2}
stuff.update(up_new)
print(stuff)

# using update to hard code a change in value on an item/key
# adding the argument directly to the update method, we are able to update
# without having to make a second dictionary.
# We can also add new items to the dictionary by adding those items
# directly as arguments to the update method.
stuff.update(food = 450, cookies = 6)
print(stuff)


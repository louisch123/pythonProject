#lists - Collection of data, can contain any/all data types in a single list,
#can contain other collections(lists, dictionaries, and tuples),
# mutable( items can be added, removed, changed), indexed ordered
"""
fruits = ["peaches", 'pears', "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)

#Append Method  - Adding to the end of the list

fruits.append("oranges")
print(fruits)

#Extend Method - Adds all elements from another list to the end of the current list

fruits.extend(years)
print(fruits)

#Remove Method - removes the first occurrence of a specified value
fruits.remove('oranges')
print(fruits)
#OR Pop Method() - Removes and returns the element at a specified index
fruits.pop(3)
print(fruits)
#OR, negative indexing - use negative indexing when the indexed number is not known
fruits.pop(-1)
print(fruits)

#Sort method() -  Can only be used for list with like data types, and places
# them in consecutive order, INT and float pt numbers can be used together
numbers = [5, 1928, 4, 17, 68]
numbers.sort()
print(numbers)"""

# IN function - use this to check membership to items in the list
fruits = ['peaches', 'pears', 'apples', 'apples', 'apples']
years = [3, '1998', 2.5, 987, '1994']

print("apple" in fruits)
print('apples' in fruits)

# Count function - Counts selected element in list
print(fruits.count('apples'))

# Index function - Checking membership and index of an element/s
print(fruits.index('apples'))


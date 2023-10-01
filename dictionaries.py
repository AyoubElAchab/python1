# Dictionaries in python
# how to create Dictionaries
# mehtod 1
band = {
    "vocals":"plant",
    "guitar":"page"
}

# method 2
band2 = dict(vocals="plant",guitar="page")

print("band = " + str(band))
print("band2 = " + str(band2))
print(type(band)) # the type is <class 'dict'>
print(len(band))  # the count of the item in the dict

## Access itams in the dict 
# ==> method 1
print(band["vocals"])
# ==> method 2 with get() function
print(band.get("guitar"))

## list all keys => get all the dict keys
print(band.keys())

## list all values => get all the dict values
print(band.values())

## list of key/value pairs as tuples => with function items
print(band.items())

# verify a key exists
print('guitar' in band)  # True
print('aze' in band)     # False

# change values in dict
band["vocals"] = "Cover"
band.update({"bass":"joj"})

print('band = ' + str(band))

# Remove items
band.pop("bass")
print('band = ' + str(band))

band['drums'] = "bonham"
print('band = ' + str(band))

# we remove the last item 
print(band.popitem()) # as a tuple
print('band = ' + str(band))

# Delete and clear
band['drums'] = "bonham"
print('band = ' + str(band))

del band['drums']
print('band = ' + str(band))


print('band2 = ' + str(band2))
band2.clear()

print('band2 clear() = ' + str(band2))
del band2
# print('band2 del = ' + str(band2))

# copy dictionaries 
band3 = band # create a reference
print('bad copy! ')
print('band3 = ' + str(band3))
print('band= ' + str(band))

band3['drums'] = "azerty"
print('band= ' + str(band))

# but this is the right way to do copy
band2 = band.copy()
band2['add'] = 'azeaze'
print('good copy!!!')
print('band = ' + str(band))
print('band2 = ' + str(band2))

# or use the dict() constructor function
band4 = dict(band)
print('good copy!!')
print('band4 = ' + str(band4))

# Nested dictionaries 
member1 = {
    "name":"Plant",
    "instrument":"vocals"
}

member2 = {
    "name":"Page",
    "instrument":"guitar"
}

band = {
    "member1":member1,
    "member2":member2
}

print("band 22 = "+str(band))
print(band["member1"]["name"])

# Sets

nums = {1,2,3,4}

nums2 = set((1,2,3,4))

print('nums sets = '+str(nums))
print('nums 2 sets = '+str(nums2))
print('type nums sets = '+str(type(nums)))
print('len nums sets = '+str(len(nums)))
print('type nums 2 sets = '+str(type(nums2)))

# no duplicate allowed
nums = {1,2,2,3}
print('nums  = '+str(nums))

# True is a dupe of 1 && False is a dupe of zero
nums = {1,True,2,False,3,4,0}
print('nums  = '+str(nums))
# the resault is => nums sets = {False, 1, 2, 3, 4}

# check if a value is in a set
print(2 in nums) # => True

# but you cannot refer to an element in the set with an index position or a key
# add new element to a set
nums.add(8)
print('nums  = '+str(nums))

# add element from one set to another
morenums = {5,6,7}
nums.update(morenums)
print('nums  = '+str(nums))

# we can use update with lists, tuples, and dict()

# merge 2 sets to create a new set
one = {1,2,3}
two = {4,5,6}

mynewset = one.union(two)
print('mynewset  = '+str(mynewset))

# keep only the duplicates => only the values
one = {1,2,3}
two = {2,3,6}
one.intersection_update(two)
print('one  = '+str(one)) # the result => one  = {2, 3}

# keep everything except the duplicates values
one = {1,2,3}
two = {2,3,6}
one.symmetric_difference_update(two)
print('one  = '+str(one))  # the result is => one  = {1, 6}



 
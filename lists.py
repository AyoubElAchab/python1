
users = ['AYOUB','EL ACHAB','KOORA']
data = ['Dave',42,True]
emptylist = []

print("AYOUB" in emptylist)
print(users[0])
print(users[-1]) 
# we use -1 for print the last item

print(users.index('AYOUB')) 
# we use index method for print the index of value "..." in a list

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

# 1. add new item in list users we use method "append"
users.append('Code01')
print("users = " + str(users))
# 2. or this method
users +=['Jeson']
print("users = " + str(users))
# 3. or extend() method
users.extend(['Robert','Jimmy'])
print("users = " + str(users))

# users.extend(data)
# print("users = " + str(users))

# add new item with the index number of the list
users.insert(0,"bob")
print("users = " + str(users))
# add new list in the 2 position
users[2:2] = ['Eddie','Alex']
print("users = " + str(users))

# replace values with other values
users[1:3] = ['Robert','joj']
print("users = " + str(users))

# remove item
users.remove('bob')
print("users = " + str(users))

# delete the last item in list
users.pop()
print("users = " + str(users))

# delete item using index of the item "del"
del users[0]
print("users = " + str(users))

# we use "clear()" for delete list competly
print("data = " + str(data))
data.clear()
print("data = " + str(data))

# sort the list with first latter A...Z first && a....z
users.sort()
print("users = " + str(users))

# sort with lower case latter a....z && A....Z
users.sort(key=str.lower)
print("users = " + str(users))

# revers order of the list the result => nums = [5,1,78,42,4]
nums = [4,42,78,1,5]
nums.reverse()
print("nums = " + str(nums))

# use sort() first  and reverse() at the same time
nums.sort(reverse=True)
print("nums = " + str(nums))

# we use sort() and reverse() but original list doesn't modifie just that print
print(sorted(nums,reverse=True))

# create  copy of original list
# method 1
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print("numscopy = " + str(numscopy))
mynums.sort()
print("mynums = " + str(mynums))
print("mycopy = " + str(mycopy))
print("nums = " + str(nums))

# check the type of the list 
print(type(nums))
# => type = list

mylist = list([1,"Neil",True])
print("nums = " + str(nums))

# Tuples 
mytuple = tuple(('Dave',42,True))
anothertuple = (1,4,2,8,2,2)
print(type(mytuple))
print(type(anothertuple))
# the type is <class = 'tuple'>
newlist = list(mytuple)
print("newlist = " + str(newlist))
newlist.append('azer')
newtuple = tuple(newlist)
print("newlist = " + str(newlist))
print("newtuple = " + str(newtuple))

(one, two, *hey) = anothertuple
print("one = " + str(one))
print("two = " + str(two))
print("hey = " + str(hey))

# the count of value "2" in tuple
print(anothertuple.count(2))

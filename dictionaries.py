Band = {
    'guitar' : 'plant',
    'vocals' : 'page'
}

Band2 = dict = {'guitar' : 'plant',
    'vocals' : 'page'}

# print(Band)
# print(Band2)
# print(type(Band))

# # length of list
# print(len(Band))

# # Access the keys
# print(Band.keys())

# # Access the values
# print(Band.values())

# # Access the items
# print(Band.items())

# print(Band["guitar"])

# print(Band["vocals"])

# print("guitar" in Band)

# print("violen" in Band)

# Updation in keys
# Band['guitar'] = 'Strings'
# print(Band)

# # Addition in keys
# Band['Burger'] = 'Salad'
# print(Band)

# Band.update({'chicken':'hen'})
# print(Band)

# # Removing values
# print(Band.pop("chicken"))
# print(Band)

# Band.popitem()
# print(Band)

# # Deleting the tablee
# Band['Burger'] = 'Salad'
# del Band['Burger']
# print(Band)

# Band2.clear()
# print(Band2)

# del Band2

# copy Dictionaries

# Bad copy

# Band2 = Band
# Band2["Drums"] = "bonds"
# print("Bad copy")
# print(Band2)
# print(Band)

# Good copy

# Band2 = Band.copy()
# Band2["Drums"] = "bonds"
# print("Good copy")
# print(Band2)
# print(Band)

# Good copy

# Band2 = Band.copy()
# Band2["Drums"] = "bonds"
# print("Good copy")
# print(Band2)
# print(Band)

# Good copy

# Band3 = dict = (Band)
# Band3["Drums"] = "bonds"
# print("Good copy")
# print(Band3)
# print(Band)

# data notation

# member1 = {
#     'name' : 'plant',
#     'instrumental' : 'guitar'
# }
# member2 = {
#     'name' : 'page',
#     'instrumental' : 'vocals'
# }
# Band = {
#     "member1" : member1,
#     "member2" : member2
# }

# print(Band)
# print(Band['member1']['name'])

# Sets

# nums = {1,2,3,4}
# anothernums = ({1,2,3,4})
# print(nums)
# print(anothernums)
# print(type(nums))
# print(len(nums))

# checking dublicate

# nums = {1,2,2,3}
# print(nums)

# # The true is 1 and false is 0 

# anothernums = {1,True,2,3,False,5,0,4}
# print(anothernums)

# adding values into sets

# nums = {1,2,3,4}
# nums.add(8)
# print(nums)

# nums.update({5,6,7})
# print(nums)

# Testing merging operations/functions

# one = {1,2,3}
# two = {4,5,6}

# print(one.union(two))

# one = {1,2,3}
# two = {2,3,6}

# one.intersection_update(two)
# print(one)

one = {1,2,3}
two = {2,3,6}

one.symmetric_difference_update(two)
print(one)


users = ["Dave", "Noman", "Shariq"]

data = ["Noman", 22, True]

emptylist = []

# print('Dave' in data)

# print(users[2])

# print(users[0:3])

# print(users[-2:-1])

# print(users.index('Noman'))

# users  += ['JOHN']
# print(users)

# users.append('ANAS')
# print(users)

# users.extend(['SIDDIQ'])
# print(users)

# users.insert(0,'WARDA')
# print(users)

# users[2:2] = ['JIMMY','MICHEAL']
# print(users)

# users[1:3] = ['TREVOR', 'JACK']
# print(users)

# users.remove('WARDA')
# print(users)

# users.pop()
# print(users)

# # del data
# data.clear()
# print(data)

# users.sort()
# print(users)


# users[1:2] = ['akib']
# print(users)

# users.sort(key=str.lower)
# print(users)

# nums = [6, 65, 1, 3, 87]
# print(nums)

# nums.sort()
# print(nums)

# nums.reverse()
# print(nums)

# print(sorted(nums, reverse=True))
# print(nums)

# copiedlist = nums.copy()
# anotherlist = list(nums)
# mycopy = nums[:]

# print(copiedlist)
# anotherlist.sort()
# print(anotherlist)
# print(mycopy)

# print(type(nums))

firstTuple = tuple(("Noman", 21, False))
anothertuple = (2, 7, 9, 4,3)

print(firstTuple)
print(type(firstTuple))
print(type(anothertuple))

newtuple = list(firstTuple)
newtuple.append("Dave")
twotuple = tuple(newtuple)
print(twotuple)

(one,*two,hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
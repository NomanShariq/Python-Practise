users = ['Dave','Noman','Shariq']

data = ['Noman',22,True]

emptylist= []

# print('Dave' in data)

# print(users[2])

# print(users[0:3])

# print(users[-2:-1])

# print(users.index('Noman'))

users  += ['JOHN']
print(users)

users.append('ANAS')
print(users)

users.extend(['SIDDIQ'])
print(users)

users.insert(0,'WARDA')
print(users)

users[2:2] = ['JIMMY','MICHEAL']
print(users)

users[1:3] = ['TREVOR', 'JACK']
print(users)

users.remove('WARDA')
print(users)

users.pop()
print(users)

# del data
data.clear()
print(data)

users.sort()
print(users)


users[1:2] = ['akib']
print(users)

users.sort(key=str.lower)
print(users)
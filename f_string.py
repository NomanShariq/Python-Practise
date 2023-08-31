person = "Dave"

coins = 3

# message = "\n %s has %s Coins Left! \n" % (person,coins)
# print(message)

# message = "\n {} has {} Coins Left! \n".format(person,coins)
# print(message)

# message = "\n {0} has {1} Coins Left! \n".format(person,coins)
# print(message)

# message = "\n {person} has {coins} Coins Left! \n".format(person=person,coins=coins)
# print(message)

player = {'person':'Noman','coins':3}

# message = "\n {person} has {coins} Coins Left! \n".format(person=player["person"],coins=player['coins'])
# print(message)

# message = "\n {person} has {coins} Coins Left! \n".format(**player)
# print(message)

## f string 

# message = f"\n {person} has {coins} coins left!"
# print(message)

# message = f"\n {person} has {5 * 6} coins left!"
# print(message)

# message = f"\n {person.lower()} has {5 * 6} coins left!"
# print(message)

# message = f"\n {player['person']} has {5 * 6} coins left!"
# print(message)


## you can pass formating options

# num = 10
# message = f'2.25 times {num} is {2.25 * num:.2f}\n '
# print(message)

# for x in range(1,11):
#     message = f'2.25 times {num} is {2.25 * num:.2f}'
#     print(message)
    
# for num in range(1,11):
#     message = f'{num} divided by 4.52 is {num / 4.52:.2%}'
#     print(message)
    

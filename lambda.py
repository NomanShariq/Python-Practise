squared = lambda number: number * number

print(squared(2))

addition = lambda number: number + 2

print(addition(12))

sum = lambda a, b: a + b

print(sum(10, 2))


def checkingnumber(x):
    return lambda num: num + x


ten = checkingnumber(10)
twenty = checkingnumber(20)

print(ten(3))
print(twenty(2))

# map

numbers = [2, 6, 4, 3, 60, 20, 50, 40]

answeroflist = map(lambda num: num * num, numbers)

print(list(answeroflist))

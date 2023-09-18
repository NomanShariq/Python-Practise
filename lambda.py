from functools import reduce


squared = lambda number: number * number

print(squared(2))

addition = lambda number: number + 2

print(addition(12))

sum_total = lambda a, b: a + b

print(sum_total(10, 2))


def checkingnumber(x):
    return lambda num: num + x


ten = checkingnumber(10)
twenty = checkingnumber(20)

print(ten(3))
print(twenty(2))

# map

numbers = [2, 6, 4, 3, 60, 20, 50, 40,65,21,39]

answeroflist = map(lambda num: num * num, numbers)

print(list(answeroflist))


###############################

total = filter(lambda num: num % 2 != 0,numbers) 

print(list(total))

################################

nombers = [1, 4, 7 ,8 ,2 ,10]

another_method = reduce(lambda acc , curr: acc + curr , nombers)

print(another_method)


another_total = sum(nombers)

print(another_total)


names = ['Noman','Shariq','King','Ben']

char_count = reduce( lambda acc , curr : acc + len(curr), names , 0 )

print(char_count)
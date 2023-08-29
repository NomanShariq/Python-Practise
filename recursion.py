



def add_one(num):
    if(num >= 9):
        return print(num + 1)
        
    
    total = num + 1
    print(total)

    return add_one(total)

add_one(0)
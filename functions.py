# def sum(num1=0,num2=0):
#     if (type(num1) is not int or type(num2) is not int):
#         return 0
#     return num1 + num2

# print(sum(1,"a"))

# def multiple_items(*kk):
#     print(kk)
#     print(type(kk))
    
# multiple_items("Noman","Shariq","monday")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_named_items(Fname = "Noman",Lname="Shariq")
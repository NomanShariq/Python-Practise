class FunckyException(Exception):
    pass

x = 2
try :
    raise FunckyException('Just Chill buddy this is checking exception basically!!')
    # raise Exception(
    #     'This is custom exception')    
    # print(x/0)
    # if not type(x) is str:
    #     print("Only strings value allowed")
except ZeroDivisionError:
    print("You can't divide by zero" )
except Exception as error:
    print(error)
else:
    print('No Errors !!')
finally:
    print('If there is error exception or no error exception i will always execute')
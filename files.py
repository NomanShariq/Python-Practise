import os


# "r" - Read - will read a file, if the file exist

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist


#---------------- Read fucntion -----------------------------------------#####

f = open("names.txt")
# print(f.read())
# print(f.read(5))


# print(f.readline())
# print(f.readline())

# for loop in f:
#     print(loop)

# try:
#     f = open("more_names.txt")
#     print(f.read())

# except:
#     print("This file doesn't Exist")

# finally:
#     f.close()

###------------- Append - Creates a file if it doesn't Exist ------------ #####

# f = open("names.txt","a")
# f.write("\nMessiii")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

#---------------------------------- Write(overwrite) ------------------- #####

# f = open("context.txt","w")
# f.write("Deleted all the context")
# f.close()

# f = open("context.txt")
# print(f.read())
# f.close()

#------------------ Write in file , Creates a file if it doesn't Exist ----#####

# There is 2 ways to create a file:

# f = open("names_list.txt","w")
# f.read()
# f.close()

# f = open("noman.txt","x")
# f.read()
# f.close()

# if os.path.exists("noman.txt"):
#     os.remove("noman.txt")
# else:
#     print("This file your searching for that doesn't Exist!")

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt","w") as f:
    f.write(content)
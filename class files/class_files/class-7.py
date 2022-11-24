# Function:

# Define function in python

# def greet():
#     print("Hello, world!")


# Calling function in Python
# greet()


# Parameter & Argument

# def greetUser(name):
#     print(f"Hello, {name}")

# userName = input("What's your name: ")
# greetUser(userName)


# Positional Argument: 

# def showFullName(f_name,l_name):
#     print(f"Your full name: {f_name} {l_name}")


# showFullName("Pritam", "Dutta")


# Keyword argument
# def add(f_num, s_num):
#     print(f"{f_num + s_num}")


# add(f_num = 5, s_num=6)


# return keyword:

# def add(n1,n2):

#     return n1+n2
    

# print(add(5,6))



# lambda function:
# lambda arguments : expression
# total = lambda a,b : a+b
# print(total(4,5))


# Recursion : Function calls itself

# 5! = 5*4*3*2*1
# 5! = 5 * 4! = 5 * 4 * 3! = 5*4*3*2! = 5 * 4* 3*2*1! = 5*4*3*2*1
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)



# print(factorial(5)) # ---> 5 * factorial(4)  ----> 5 * 4 * factorial(3) ---> 5 * 4 * 3 * factorial(2) ---> 5*4*3*2*factorial(1) ---> 5*4*3*2*1 =120


# Caesar cipher : encode decode a msg

# What do you want to do?
# 1 for encode and 2 for decode: 1

# Enter your message: Hi, abc!
# enter the secret key: 2

# Your secret message is: jk, cde!


# What do you want to do?
# 1 for encode and 2 for decode: 2

# Enter your message: jk, cde!
# enter the secret key: 2

# Your decoded message is: Hi, abc!


# Dictionary, Tuple, Tkinter

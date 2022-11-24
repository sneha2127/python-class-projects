# Loops - for loop and while loop

# while loop: execute a block of code until the codition remains true

# Syntax:
# print 1 to 10

# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# Infinity:

# while True:
#     print("Hello")


# for loop : Execute a block of code for given of range

# syntax: 
# for var in range(start,stop):
#   block of code


# print 1 to 10 

# for i in range(1,11):
#     print(i)



# Print the odd numbers between 1 to 10

# for i in range(1,11):
#     if i%2 !=0:
#         print(i)



# break and continue

# print 1 to 10 but if  i == 5 then brak the loop with a msg 

# for i in range(1,11):
#     print(i)
#     if i == 5:
#         print("You got 5!")
#         break




# continue:
# print 1 to 10 but skip 3 and 5 


# for i in range(1,11):
#     if i == 3 or i == 5:
#         continue

#     print(i)


# project : Number Guessing Game v-1 using loops
# chances = 5



# Python time module
import time


# time.time()  ---> The seconds from january 1,1970

# print(time.time())


# Excution time find

# initial = time.time()
# for i in range(1,101):
#     print(i)

# end = time.time()

# print(f"Execution time: {end-initial}")


# local time

# print(time.asctime(time.localtime(time.time())))


# strftime():

# print(time.strftime("%Y"))
# print(time.strftime("%m"))
# print(time.strftime("%D"))
# print(time.strftime("%H:%M:%S"))
# print(time.strftime("%d"))



# Digital Clock
import os

while True:
    print(f'Current time: {time.strftime("%H:%M:%S %p")}')
    time.sleep(1)
    os.system('cls')
    


# next topic - Function and Dictionary
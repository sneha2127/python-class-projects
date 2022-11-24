# List:
# syntax:
# numbers = [elem1, elem2, elem3, ...]


numbers = [1,2,3,4,5,6,7]
# print(numbers)


# empty list:
# student_bio = []

# Access each elem
# print(numbers[0])

# List Concatiation
# boys = ["Rahul", "Rohit"]
# girls = ["Shreya", "Mini"]

# Friends = boys + girls

# print(Friends)


# List Methods
# adding value

# append(value): It adds a value at the end of the list
# numbers.append(8)
# print(numbers)

# extend(list): It add the values of the given list at the end of the list
# numbers.extend([9,10,11,12])
# print(numbers)


# insert(index,value): Add the give value in the particular index
# numbers.insert(4,20)
# print(numbers)


# Removing methods
# remove(value): It removes the given value from the list
# numbers.remove(6)
# print(numbers)


# pop(index): It remove the given index value and returns the element
# removed_item = numbers.pop(2)
# print("You removed " + str(removed_item))
# print(numbers)

# pop() without index: It removes last element

# Update value:

# student_bio = ["Pritam", 21]
# student_bio[1] = 22
# print(student_bio)

# count(value): It returns the occurance of the element
characters = ["c","o","o","l"]
# print(characters.count("o"))


# index(value): It returns the index of the given value
# print(characters.index("o"))

# print(characters.index("o",2))



# String Method:
# split(): String to List 
# msg = "hello, world!"

# words = msg.split(",")
# print(words)


# join()

# word = "".join(characters)
# print(word)



# random Module: Randomisation work 

# Module: One python file
import random

# random integer
# print(random.randint(1,10))


# random float
# print(random.random())


# choice(list)

# parameters = ["Rock","Paper","Scissor"]
# print(random.choice(parameters))

# suffle(list):
# random.shuffle(parameters)
# print(parameters)


# Number Guessing Game v-0
# Enter the guess number between 1 to 20: 5
# Sorry, you choose wrong number


# Enter the guess number between 1 to 20: 7
# You win!

# Concept: If Else, Random module


# Rock Paper Scissor v-0:  
# Enter your choice: rock
# You choose: rock
# Computer choose: Paper
# Computer win


# Rules: 
# Rock > Scissor 
# Scissor > Paper
# Paper > Rock


# Concept:
# List , Random, Nested if condition



# Next day Topic - 
# Loops, Math module, Function basic
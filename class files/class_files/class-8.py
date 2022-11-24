# Dictionary: Key:Value

# Define a dictionary:

personal_data = {
    "name":"Pritam",
    "age" : 21,
    "DOB" : "02/11/2000"
}

# print(personal_data)


# Access each value
# print(personal_data["name"])


# for loop on dictionary
# for var in personal_data:
#     print(personal_data[var])


# Dictionary method

# for key,value in personal_data.items():
#     print(f"{key}:{value}")


# update: 
# personal_data.update({"phone":9382637127})
# print(personal_data)


# add key:value
# personal_data["email"] = "info.pritcast@gmail.com"
# print(personal_data)


# Edit a value 
# personal_data["name"] = "Rahul"
# print(personal_data)


# Remove Method
# delete_age = personal_data.pop("age")
# print(personal_data)
# print(delete_age)


# List of keys:
# print(list(personal_data.keys()))
# List of values:
# print(list(personal_data.values()))


# ---------------------------------------------------



# File Handling

# Reading File

# file = open('demo.txt', 'r')
# print(file.read())
# tasks = file.readlines()
# for task in tasks:
#     if "\n" in task:
#         task = task[:-1]
#     else:
#         task=task

#     print(task)
# file.close()


# Write on a file
# file = open('demo.txt', 'w')
# file.write("Welcome to this Python tutorial!")
# print("Done")
# file.close()


# Append on a file
# file = open('demo.txt', 'a')
# file.write("\nThis is all about Python!\n")
# print("Done")
# file.close()

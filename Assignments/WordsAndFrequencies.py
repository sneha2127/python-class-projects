text1 = "learning to code is learning to create and innovate"

word_list = text1.split(" ")

word_dictionary ={}

for word in word_list:
    if word in word_dictionary.keys():
        word_dictionary[word] +=1
    else:
        word_dictionary[word] = 1

for key in word_dictionary.keys():
    print(f"{key} : {word_dictionary[key]} times.")
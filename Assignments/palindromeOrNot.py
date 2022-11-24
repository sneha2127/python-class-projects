text_string = input("Enter the string you want to perform palindrome check on : ")

if text_string[::-1] == text_string :
    print(f" {text_string} is a palindrome!")
else:
    print("It's not a palindrome")
# Ask the user for a string and print out whether
# this string is a palindrome or not.

user_string = input("Enter a word: ").lower()

def reverse(string):
    new_string = ""
    for index in range(len(string) -1, -1, -1):
        new_string = new_string + string[index]
    return new_string


def is_palindrome(reversed):
    if(reversed == user_string):
        print("{0} is a palindrome.".format(user_string))
    else:
        print("{0} is NOT a palindrome.".format(user_string))

is_palindrome(reverse(user_string))

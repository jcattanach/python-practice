# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check
# and one number to divide by.
# If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

number = int(input("Enter a number: "))

def is_even(number):
    if(number % 2 == 0 and number % 4 != 0):
        print("{0} is an EVEN number.".format(number))
    elif(number % 4 == 0):
        print("{0} is an EVEN number and is a multiple of 4.".format(number))
    else:
        print("{0} is an ODD number.".format(number))


is_even(number)

check = int(input("Enter a second number: "))

def is_multiple(number, check):
    if(number % check == 0):
        print("{0} is divisible by {1}.".format(number, check))
    else:
        print("{0} is NOT divisible by {1}.".format(number, check))

is_multiple(number, check)

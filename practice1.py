# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year
# that they will turn 100 years old.




name = input("Enter your name: ")
age = int(input("Enter your age: "))

def find_birth_year(age):
    birth_year = 2018 - age
    return birth_year

def when_one_hundred(birth_year):
    year_hundred = birth_year + 100
    return year_hundred

answer = when_one_hundred(find_birth_year(age))
print("{0}, you will turn 100 years old in the year {1}.".format(name, answer))

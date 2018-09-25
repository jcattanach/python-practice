# Take two lists and write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.


list_one = [1,5,7,9,14,12,3,6,8]
list_two = [1,7,4,5,3,9,12]
list_common = []
for index in list_one:
    for index_2 in list_two:
        if(index == index_2):
            list_common.append(index)

print(sorted(list_common))

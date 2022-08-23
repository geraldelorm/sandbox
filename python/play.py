from itertools import permutations

# Getting input from user e.g "1 2 3" and splitting it into an arr
arr1 = input("Enter the numbers: ").split(" ")
arr2 = input("Enter the numbers: ").split(" ")

# converting the second list into a tuple to compare with permumations which are tuples
arr2 = tuple(i for i in arr2)

# function to compare permutations with second user input
def compare(perm, list):
    for item in perm:
        if item == list:
            return True
    return False

perms = permutations(arr1)

# Printing result of comparism
print(compare(perms, arr2))
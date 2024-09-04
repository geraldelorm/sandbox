import array as array 

arr = array.array('i', [1, 2, 3])
print("The new created array is: ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")

print()

# arr2 = array.array('d', [2.5, 3.2, 3.3])
# print("The new created array is: ", end=" ")
# for i in range(0, 3):
#     print(arr2[i], end=" ")

#inserting array using insert() method
print("After insering into the array using the insert() method: ", end='')
arr.insert(0, 4)
for item in arr:
    print(item, end=' ')
print()

print("After updating the array using the append() method: ", end=' ')
arr.append(5)
for item in arr:
    print(item, end=' ')
print()


#Accessing an element inan array
print("Element at index 2 in arr is: ", arr[2])
print("Element at index 0 in arr is: ", arr[0])
print()


#Removing an element form an array
print("Removing the last element with pop()", arr.pop())
print(arr)
print

print("Removing the forst element with pop(0)", arr.pop(0))
print(arr)
print()


#Remove from array using value
print("Append 9 to arr")
arr.append(9)
print(arr)
print("Remove 9 from arr")
arr.remove(9)
print(arr)
print()

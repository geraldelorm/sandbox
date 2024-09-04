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



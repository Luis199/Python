from array import array
arr1 = array('i', [1,2,3,4,5,6,7,8,9])
print(arr1.typecode)
print("Array 1 item size: ", arr1.itemsize)


arr1.insert(0,0)
arr1.append(22)
l = arr1.tolist

print(arr1)
print(l)
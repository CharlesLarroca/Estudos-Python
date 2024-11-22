array = [32,4,56,99,2,5]

def find_largest(arr):
  if not arr:
    return 'Array is empty'
  
  largest = arr[0]
  
  for element in arr:
    if element > largest:
      largest = element
   
  return largest
 
print(f'The largest element in the array is {find_largest(array)}')
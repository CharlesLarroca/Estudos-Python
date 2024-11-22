def split_array(arr, k):
  
  if k <= 0 or k >= len(arr):
    return arr
  
  first_part = arr[:k]
  second_part = arr[k:]
  
  result = second_part+first_part
  
  return result

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = 5

result = split_array(array, k)

print(f'The Original Array is {array}')
print(f'The Split Array is {result}')
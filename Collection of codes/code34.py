def rotate_array(arr, d):
  n = len(arr)
  
  if d < 0 or d >= n:
    return 'Invalid Rotation'
  
  #creates a new arr with the length of n fulled with 0 [0,0,0,0]
  rotate_arr = [0] * n
  
  for i in range(n):
    rotate_arr[i] = arr[(i+d)%n]
  return rotate_arr

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d = -1

result = rotate_array(array, d)

print(f'The Original Array is {array}')
print(f'The Rotate Array is {result}')
  
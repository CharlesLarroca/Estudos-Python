array = [1, 2, 3, 4]

ans = sum(array)

print(f'The sum of the array is {ans}')

def calculate_sum_array(arr):
  total = 0
  
  for element in arr:
    total += element
  
  return total

print(f'The sum of the array is {calculate_sum_array(array)}')
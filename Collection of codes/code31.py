def calculate_sum_of_cube(n):
  if n <= 0:
    return 0
  else:
    total = sum([i**3 for i in range(1, n + 1)])
    return total
  
num = int(input('Enter the value of n: '))

if num <= 0:
  print('Please insert a positive integer')
else:
  print(f'The cube sum of the first {num} natural numbers is {calculate_sum_of_cube(num)}')
import math

def calculate_log(n):
  if n < 0:
    print('Enter a positive number')
  else:
    return math.log(n)

num = float(input('Enter the number: '))

print(f'The natural logarithm of {num} is {calculate_log(num)}')
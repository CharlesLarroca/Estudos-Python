num = int(input('Enter the number: '))

factorial = 1

if num < 0:
  print('Does not exist factorial for negative numbers')
elif num == 0:
  print(f'The factorial number of {num} is 1')
else:
  for i in range(1, num+1):
    factorial = factorial*i
  print(f'The factorial number of {num} is {factorial}')
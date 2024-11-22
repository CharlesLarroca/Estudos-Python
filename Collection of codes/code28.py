def recur_factorial(n):
  if n == 1:
    return n
  else:
    return n*recur_factorial(n-1)


num = int(input('Enter the number: '))

if num < 0:
  print('Sorry, factorial does not exist for negative number')
elif num == 0:
  print(f'The factorial of {num} is 1.')
else:
  print(f'The factorial of {num} is {recur_factorial(num)}')
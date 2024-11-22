def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

print('Select a Operator')
print('1 - Add')
print('2 - Subtract')
print('3 - Multiply')
print('4 - Divide')

while True:
  choice = input('Enter choice (1/2/3/4): ')
  
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input('Enter the first number: '))
      num2 = float(input('Enter the second number: '))
    except ValueError:
      print('Invalid input. Please enter a number.')
      continue
  
    if choice == '1':
      print(f'The add of {num1} + {num2} is equal to {add(num1, num2)}')
    elif choice == '2':
      print(f'The subtract of {num1} - {num2} is equal to {subtract(num1, num2)}')
    elif choice == '3':
      print(f'The multiply of {num1} * {num2} is equal to {multiply(num1, num2)}')
    elif choice == '4':
      print(f'The divide of {num1} / {num2} is equal to {divide(num1, num2)}')
      
    next_calculation = input("Let's do next calculation? (yes/no)")
    
    if next_calculation == 'no':
      break
  else:
    print('Invalid Value')
      
      

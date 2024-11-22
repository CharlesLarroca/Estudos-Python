def compute_hfc(x, y):
  if x > y:
    smaller = y
  else:
    smaller = x
    
  for i in range(1, smaller+1):
    if x % i == 0 and y % i == 0:
      hfc =  i
  return hfc

num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))

print(f'The HFC of {num1} e {num2} is {compute_hfc(num1, num2)}')
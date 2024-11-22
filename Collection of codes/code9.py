import math

#Enter Coefficients
a = float(input('Enter coefficient a: '))
b = float(input('Enter coefficient b: '))
c = float(input('Enter coefficient c: '))

discriminant = b**2 - 4*a*c

#check if discriminant is positive, negative or zero

if discriminant > 0:
  #two real and distinct root
  root1 = (-b + math.sqrt(discriminant)) / (2*a)
  root2 = (-b - math.sqrt(discriminant)) / (2*a)
  print(f'Root 1 > 0: {root1}')
  print(f'Root 2 > 0: {root2}')
elif discriminant == 0:
  #one real root
  root = -b / (2*a)
  print(f'Root == 0: {root}')
else:
  #complex root
  real_part = -b / (2*a)
  imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
  print(f'Root 1 < 0: {real_part} + {imaginary_part}i')
  print(f'Root 2 < 0: {real_part} - {imaginary_part}i')

num = int(input('Enter a number: '))

num_str = str(num)
num_digit = len(num_str)

sum_of_power = 0
temp_num = num

while temp_num > 0:
  digit = temp_num % 10
  sum_of_power += digit ** num_digit
  temp_num //= 10 #the //=10 remove the last digit, using the floordiv 
  
if sum_of_power == num:
  print(f'{num} is an Armstrong Number')
else:
  print(f'{num} is not an Armstrong Number')
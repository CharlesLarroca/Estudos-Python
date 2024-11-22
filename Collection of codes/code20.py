lower = int(input('Enter the lower limit of the interval: '))
higher = int(input('Enter the higher limit of the interval: '))

for num in range(lower, higher+1):
  order = len(str(num))
  temp_num = num
  sum = 0

  while temp_num > 0:
    digit = temp_num % 10
    sum += digit ** order
    temp_num //= 10 #the //=10 remove the last digit, using the floordiv 
    
  if num == sum:
    print(num)
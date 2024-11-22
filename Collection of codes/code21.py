limit = int(input('Enter the limit of the natural numbers: '))

sum = 0

for n in range(1, limit+1):
  sum += n

print(f'The sum of natural numbers up to {limit} is {sum}')
nTerms = int(input('How much terms? '))

n1, n2 = 0, 1
count = 0

if nTerms <= 0:
  print('Insert a integer number.')
elif nTerms == 1:
  print(f'Fibonacci sequence upto {nTerms}:')
  print(n1)
else:
  ('Fibonacci Sequece:')
  while count < nTerms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
year = int(input('Enter the year: '))

#rules
#divide by 100 is a century, and a century divide by 400 is a leap
#not divided by 100 means not a century year
#year divided by 4 is a leap year
#if not divided by both 400 (century year) and 4 (not century year)
#year is not leap year
if (year%400 == 0) and (year%100 == 0):
  print('{0} year is a leap'.format(year))
elif (year%4 == 0) and (year%100 != 0):
  print('{0} year is a leap'.format(year))
else:
  print('{0} year is not leap'.format(year))
  
  
  

def calculate_BMI(weight, height):
  return round(weight/(height*height), 2)

print('Welcome to the BMI calculator.')

w = float(input('Enter your weight in kg: '))
h = float(input('Enter your height in meters: '))

bmi = calculate_BMI(w, h)
print(f'Your BMI is {bmi}')

if bmi <= 18.5:
  print("You are underweight.")
elif 18.5 < bmi <= 24.9:
 print("Your weight is normal.")
elif 25 < bmi <= 29.29:
 print("You are overweight.")
else:
 print("You are obese.")

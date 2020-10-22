# BMI calculator

# Ask for the person's details
print("What is your name?")
name = input()
print("How old are you (in years)?")
age = int(input())
print("How tall are you (in meters)?")
height = float(input())
print("How much do you weigh (in kilograms)?")
weight = float(input())

#height squared

height = height * height
bmi = float(weight/height)

# Display BMI calculation
print(name + " you are " + str(age) + " years old and your BMI is " 
+ str("{:.2f}".format(bmi)))

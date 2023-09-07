# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
res = weight / (height ** 2)
print(f"{weight} ÷ ({height} x {height}) = {res}")
if res <= 0:
    print(f"Your BMI is wrong, please enter valid values.")
elif res < 18.5:
    print(f"Your BMI is {round(res)}, you are underweight.")
elif 18.5 <= res < 25:
    print(f"Your BMI is {round(res)}, you have a normal weight.")
elif res >= 25 and res < 30:
    print(f"Your BMI is {round(res)}, you are slightly overweight.")
elif res >= 30 and res < 35:
    print(f"Your BMI is {round(res)}, you are obese.")
elif res >= 35:
    print(f"Your BMI is {round(res)}, you are clinically obese.")


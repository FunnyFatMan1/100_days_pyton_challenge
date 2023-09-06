age = int(input("What is your current age? "))
if age<0 or age>90:
    print("enter a avg age")
days=(90-age)*365
weeks=(90-age)*52
months=(90-age)*12
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
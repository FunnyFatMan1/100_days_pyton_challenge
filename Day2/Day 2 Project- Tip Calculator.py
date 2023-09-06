print("Welcome to the tip calculator!")
bill=int(input("What was the total bill? $"))
tip=int(input('How much tip would you like to give? 10, 12, or 15? '))
ppl=int(input('How many people to split the bill? '))
res=(bill+(bill/tip))/ppl
print(f"Each person should pay: ${res}")

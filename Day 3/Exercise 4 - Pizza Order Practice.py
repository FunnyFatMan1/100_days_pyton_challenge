print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill=0
if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill += 20
elif  size.upper() == "L":
    bill += 25
else:
    print("Please enter a valid pizza size")
if add_pepperoni.upper() == "Y" and size.upper() == "S":
    bill += 2
elif add_pepperoni.upper() == "Y" and (size.upper() == "M" or size.upper() == "L"):
    bill += 3
if extra_cheese.upper() == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
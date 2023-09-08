import random
names_string = input("Enter names: ")
names = names_string.split(", ")
random_name = random.randint(0, len(names)-1)
print(f"{names[random_name]} is going to buy the meal today!")




# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_string=name1+name2
lower_s=combined_string.lower()
t = lower_s.count("t")
r = lower_s.count("r")
u = lower_s.count("u")
e = lower_s.count("e")
true=t+r+u+e
l=lower_s.count("l")
o=lower_s.count("o")
v=lower_s.count("v")
e=lower_s.count("e")
love=l+o+v+e

love_score=str(true)+str(love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")


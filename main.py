import random
jackpot = random.randint(1,101)
user_input =  int(input("Guess the number:"))
counter = 1
while  user_input != jackpot:
    if user_input < jackpot:
        print("Guess higher")
    else:
        print("Guess lower")
    user_input = int(input("Guess the number:"))
    counter+=1
print("You have hit the jackpot!")
print(f"You took {counter} chances.")

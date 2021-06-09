import random
answer = random.randint(1, 10)

print("please guess number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess == answer:
        print("well done")
    else:
        print("wrong again")
elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done")
    else:
        print("wrong again")
else:
    print("you got it! first try")

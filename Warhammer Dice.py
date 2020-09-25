import random

n = int(input("Enter your skill value: "))

roll = random.randint(1, 100)
print(f"Skill value is {n}. You rolled {roll}.")

if roll in range(96, 100) and n < roll:
    print(
        f"Critical failure. Test failed by: {roll - n}.That is {roll // n} of your skill.")
elif roll in range(1, 4) and n > roll:
    print(f"Wow! Critical success! Test beaten by {n - roll}. That is {n // roll} of your skill.")
elif roll <= n:
    print(f"Sucess! Test beaten by {n - roll}. That is {n // roll} of your skill.")
elif roll > n:
    print(f"Test failed by: {roll - n}. That is {roll // n} of your skill.")

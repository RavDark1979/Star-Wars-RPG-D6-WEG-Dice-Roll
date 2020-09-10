import random

n = int(input("Enter dice pool: "))
x = int(input("Enter test difficulty value: "))

lst_num = []

while n != 0 and len(lst_num) < n:
    random.randint(1, 6)
    lst_num.append(random.randint(1, 6))

sum_rolls = sum(lst_num)

if x > sum_rolls:
    print("Test failed!")
elif x <= sum_rolls:
    print("Test was sucessful!")

if lst_num[-1] == 1:
    lst_num.remove(min(lst_num))
    lst_num.remove(max(lst_num))
    print("Complication - I got a bad feeling about this...")

while lst_num[-1] == 6:
    lst_num.append(random.randint(1, 6))
    print("Advantage gained, but don't get cocky!!")


sum_rolls = sum(lst_num)

print(f'Rolled: {lst_num}')
print(f'Total: {sum_rolls}')


import random

n = int(input("Enter Sense dice pool: "))
x = int(input("Enter number of shots: "))
y = int(input("Enter the number of arcs you wish to cover (min: '1', max: '4'"))

lst_num = []

for _ in range(n):
    lst_num.append(random.randint(1, 6))


if lst_num[-1] == 1 and n >= 2:
    lst_num.remove(min(lst_num))
    lst_num.remove(max(lst_num))
    print("Complication - I got a bad feeling about this...")

elif lst_num[-1] == 1 and n == 1:
    lst_num.remove(min(lst_num))
    print("Complication - I got a bad feeling about this...")


elif lst_num[-1] == 6:
    while lst_num[-1] == 6:
        lst_num.append(random.randint(1, 6))
        print("Advantage gained, but don't get cocky!!")

sum_rolls = sum(lst_num)
deflect_diff = x * 3
deflected = sum_rolls // 3
not_deflected = x

print(f'Rolled: {lst_num}, Total: {sum_rolls}')
print(f'Total deflect difficulty: {deflect_diff}')

if deflect_diff <= sum_rolls:
    print("You have deflect all shots")

elif deflect_diff > sum_rolls:
    print(f'You have deflected {deflected} shot(s).'
          f'You were hit with {not_deflected - deflected} shot(s).')

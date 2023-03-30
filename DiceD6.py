def skillroll():
    import random

    n = int(input("Enter dice pool: "))
    x = int(input("Enter test difficulty value: "))

    lst_num = []

    for _ in range(n):
        lst_num.append(random.randint(1, 6))

    sum(lst_num)

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

    if x > sum_rolls:
        print("Test failed!")

    elif x <= sum_rolls:
        print("Test was sucessful!")

    print(f'Rolled: {lst_num}')
    print(f'Total: {sum_rolls}')

    again = input("Again? 'y' to continue  ")
    if again == "y":
        skillroll()
    else:
        print("May the Force be with you")


skillroll()

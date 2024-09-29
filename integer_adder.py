user_entered = int(input('Enter an integer, the input ends if it is 0: '))

if user_entered == 0:
    print('No numbers are entered except 0')
    exit()
else:
    acc = 0
    acc_pos = 0
    acc_neg = 0
    numbers = []

    while user_entered != 0:
        if user_entered > 0:
            acc_pos += 1
            numbers.append(user_entered)
        elif user_entered < 0:
            acc_neg += 1
            numbers.append(user_entered)
        elif user_entered == 0:
            break

        acc += user_entered

        user_entered = int(input('Enter an integer, the input ends if it is 0: '))

    if len(numbers) != 0:
        avg = acc / len(numbers)
    else:
        avg = 0

    print(f'The number of positives is {acc_pos}')
    print(f'The number of negatives is {acc_neg}')
    print(f'The total is {acc}')
    print(f'The average is {avg:.2f}')
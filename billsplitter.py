import random

names = {}
print('Enter the number of friends joining (including you):')
num_of_friends = int(input())
if num_of_friends < 1:
    print()
    print('No one is joining for the party')
else:
    print()
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(num_of_friends):
        names[input()] = 0
    print('Enter the total bill value:')
    total_bill = float(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    if answer == "Yes":
        lucky = random.choice(list(names.keys()))
        print(lucky, 'is the lucky one!')
        for i in names:
            names[i] = round(total_bill / (num_of_friends - 1), 2)
        names[lucky] = 0
        print(names)
    else:
        print('No one is going to be lucky')
        for i in names:
            names[i] = round(total_bill / num_of_friends, 2)
        print(names)

#i = int(input('Enter number : '))
for i in range(2, 11):
    print(f'Mnoshennia na {i}:\n', end= '')
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}\n', end= '')
    print('')
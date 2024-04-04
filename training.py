

# i = int(input('Enter number: '))
# while i % 2 == 0:
#         print(i)
#         i -= 1

# i = int(input('Enter number: '))
# for n in list(range(0, i, 2)):
#     print(n, end=' \n')

list2 = {'name': 'Vasya', 'second_name': 'petrovich'}
print(list2['name'])

list1 = [1, 2, 3, 4, ['a', 'b', 'c', 'd'], 5, 6, 7]
print(list1[4][3])

def say(message, times=1):
    print(message * times)

say('Привіт '+' Світ' * 5) 


# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 != 0:
#         result = "Positive odd number"
#         print(result)
#     else:
#         result = "Positive even number"
#         print(result)
# elif num < 0:
#     result = "Negative number"
#     print(result)
# else:
#     result = "It is zero"
#     print(result)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# while num >= 0:
#     sum += num
#     num -= 1
# print(sum)


# string = 'Hello World!'
# length = 15
# def format_string(string, length):
#     if len(string) >= length: return string
#     elif len(string) < length:
#         string = " " * ((length - len(string)) // 2)
#         return string
# print(string)

# balance = 0.7 + 0.6
# print('result1:', balance)
# if round(balance, 1) == 1.3:
#     print('result2: Ok')
# else:
#     print('not')

# Задаємо конкретне число
# num = int(input('Enter number: '))

# # Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)

# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state)

# num_one, num_two = 0, 1
# for i in range(10):
#     print(i, end=' ')
#     num_one, num_two = num_two, num_two = num_one

# string = 'Hello'
# length = 6
# def format_string(string, length):

#     if len(string) >= length: 
#         return string
#     elif len(string) < length:
#         whitespaces = (length - len(string)) // 2
#         string = ((" " * whitespaces) + string)
#         return string
#     format_string(string, length)

# alphabet = "abcdefghiaklmaopqratuvwxyz"
# for char in alphabet:
#     if char == "a":
#         continue
#     print(char, end=" ")


# i = int(input('Enter number: '))
# for n in list(range(0, i, 2)):
#     print(n, end=' \n')

# list2 = {'name': 'Vasya', 'second_name': 'petrovich'}
# print(list2['name'])

# list1 = [1, 2, 3, 4, ['a', 'b', 'c', 'd'], 5, 6, 7]
# print(list1[4][3])

# def say(message, times=1):
#     print(message * times)

# say('Привіт '+' Світ' * 5) 


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

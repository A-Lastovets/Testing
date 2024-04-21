def bot_func(us_list: list, data_type):

    new_list = []
    for element in us_list:

        if not isinstance(element, data_type):
            new_list.append(element)
            
    return new_list

#y_list = ["senior", "11","switcher", 11, "name", 123]


print(bot_func(["senior", "switcher", 1, "name", "1", "hello"], str))

    
# my_str = "How can mirrors be real if our eyes aren’t real" 
# a = "t" 
# b = "real"
# x = my_str.title() + a + ' ' + b.title()
# print(x)


# text = input("Enter text: ")
# for letter in text:
#     if letter == "’":
#         text = text.replace("’", "")
# print("Result: \n", text.title())


# s = "\nHow can mirrors be real if our eyes aren’t real"
# for x in s:
#     if x == "’":
#         s = s.replace("’", "")
# print(s.title())


# s = input('Enter text: ').title()
# i = 0
# while i < len(s):
#     print(s[i:i+1], end='')
#     i += 1 


# for letter in text:
#     if letter == "_a":
#         text = text.replace("_a", "’")
#         print(text, end=' ')

#--------------------------------------------------------
# n = int(input('Enter number of last range: '))
# s = 0
# for i in range(n+1):
#     s += i
# print(f'Sum below numbers 1 to {n}: ', s)


# n = int(input('Enter number of last range: '))
# s = 0
# i = 1
# while i <= n:
#     s = i + s
#     i += 1
# print(f'Sum below numbers 1 to {n}: ', s)


# n = int(input('Enter number of last range: '))
# print(f'Sum below numbers 1 to {n}: ', int((n * (n + 1)) / 2), end =' ')

#-----------------------------------------------------------------------------------------------------

# Написать функцию my_func(a: int).

# Если аргумент будет равен 1 -> вернуть a * 10, 
# если a равен 20 -> вернуть a * 2, 
# если a равен 40 -> вернуть a * 3. 
# Во всех остальных случаях, вернуть строку: Не знаю как обработать данное число = a

# def my_func(a: int):
#     if a == 1: 
#         result = 10
#     elif a == 20:
#             result = a * 2
#     elif a == 40:
#             result = a * 3
#     else:
#         result = f"Не знаю как обработать данное число = {a}"
#     return result
# print(my_func(1))

# import random

# numbers = [1, 20, 40, None]
# random_numbers = random.choice(numbers)

# match random_numbers:
#     case 1:
#         print(f"Result: {random_numbers * 10}")
#     case 20:
#         print(f"Result: {random_numbers * 2}")
#     case 40:
#         print(f"Result: {random_numbers * 3}")
#     case _:
#         print(f"Не знаю как обработать данное число = {random_numbers}")

#---------------------------------------------------------------------------------------------------


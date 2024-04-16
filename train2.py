fruits = {
    1: "apple", 
    2: "banana",
    3: "orange"
    }
print(input(f"Please choise one fruit : {1} - apple, {2} - banana, {3} - orange : \n"))

match fruits:
    case "apple" if fruits == 1:
        print("This is an apple.")
    case "banana" if {2}:
        print("This is a banana.")
    case "orange" if {3}:
        print("This is an orange.")
    case _:
        print("Unknown fruit.")
# #----------------------------------------------------------------------------------------------------
# import random
 
# fruits = ["apple", "banana", "orange"]
# random_fruit = random.choice(fruits)

# match random_fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")
#-----------------------------------------------------------------------------------------------------

# def foo():
#     value_a = 4
#     value_b = 8
#     return value_a + value_b
# sum_value = foo()
# print(sum_value)
#-----------------------------------------------------------------------------------------------------
# def add(value_one: int, value_two: int) -> int:

# # Function af adding two numbers
# # input:
# # :param value_one: integer
# # :param value_two: integer
# # Output:
# # :return: integer

#     sum_of_two_numbers = value_one + value_two
#     return sum_of_two_numbers

# result: int = add(2,4)
# print(result)
#-----------------------------------------------------------------------------------------------------

# def multiply(number_one, number_two, number_three=None):
#     print(number_three, end=' ')
#     if number_three is None:
#         return number_one * number_two
#     else:
#         return number_one * number_two * number_three
    
# print(multiply(2,3))
# print(multiply(2, 3, 5))

#--------------------------------------------------------------------------------------------
# def add(number_one, number_two):
#     return number_one * number_two
# print(add(3, 4))
# # print(add(3, 4, 5))  #  TypeError: add() takes 2 positional arguments but 3 were given
#--------------------------------------------------------------------------------------
# def sum_af_all_numbers(*numbers):
#     sum = 0
#     for value in numbers:
#         try:
#             sum += float(value)
#         except TypeError:
#             continue
#         except ValueError:
#             continue
#     return sum

# print(sum_af_all_numbers(1,2,3,4,5,6,7,8))
#--------------------------------------------------------------------------------------------

# def sum_af_all_numbers(*numbers):
#     sum = 0
#     for value in numbers:
#         try:
#             sum += float(value)
#         except TypeError:
#             continue
#         except ValueError:
#             continue
#     return sum

# print(sum_af_all_numbers(1,2,3,4,5, '1000', 6,7,8,9,0, 7.7, 'true', False, 90, -100, sum([1,2,3,4,99])))
# #--------------------------------------------------------------------------------------------
# def gretting(**kwargs):
#  #   print(kwargs)
#     name = kwargs.get("name", "Unknown")
#     age = kwargs.get("age", 18)
#     print(f"Hello {name}, you are {age} years old")
# #gretting(name="Oleh")
# gretting(name="Oleh", age=100)
#--------------------------------------------------------------------------------------------
# def print_input(value, *transport, hello, **text):
#     print(value)
#     print(transport)
#     print(text)
#     print(text['may']/9)
#     print(hello)

# print_input(78, 246, 'qwerty', 'dsgdf345:as', 3543456, 50, hello="Python", may=45)
#--------------------------------------------------------------------------------------------

# def foo():
#     a = 4
#     b = 8
#     print(f"a = {a}, b = {b}")
#     return a+b
# print(foo())

# print(" " * 10)
# #----------------------------------------------------------
# password = 1234
# def security(passwd):
#     def divide():
#         nonlocal passwd
#         print(passwd)
#         return passwd / 2
#     return divide()
# print(security(password))
# #----------------------------------------------------------
# def fibonachi(number):
#     return number if number == 0 or number == 1 else fibonachi(number-2) + fibonachi(number-1)
# print(fibonachi(11))
#----------------------------------------------------------
# def format_string(string, length):
#     if len(string) > length:
#         return string
#     else:
#         total_spaces = length - len(string)
#         space_left = total_spaces // 2
#         space_right = total_spaces - space_left
#         return " " * space_left + string + " " * space_right
#--------------------------------------------------------------------------
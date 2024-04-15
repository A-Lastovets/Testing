# fruits = ["banana", "orange", "apple"]
# prices = [10, 20, 30]

# for value in range(len(fruits)):
#     print(fruits[value],":", prices[value])
    
# count = 0
# for i in fruits:
#     print(i,":", count)
#     count += 1

# for name, cost in zip(fruits, prices):
#     print(name + ':', cost)

# i = 0
# while i < len(fruits):
#     print(fruits[i] + ':', prices[i])
#     i += 1

# for index, value in enumerate(prices):
#     print(index, value)

print("-" * 100)   #------------------------------------------------------------------------------------------------------

list1 = list("hello")
for i in range(len(list1)):
    print(f"{i} : {list1[i]}")

print("-" * 100)   #------------------------------------------------------------------------------------------------------
# s = '\nHello World'
# i = 0
# while i < len(s):
#     print(s[i:i + 1], '', end= '')
#     i += 1
# #----------------------------------------------------
# my_list = ["Mykola Kuzmin", "Toxa", "CrazyTosser", "Evgeniya", "Vitaliy", "Eugene"]

# switcher, *seniors = my_list

# print(f"{switcher=}")
# print(f"{seniors=}")
print("-" * 100)   #------------------------------------------------------------------------------------------------------

my_list = ["Mykola Kuzmin", "Toxa", "CrazyTosser", "Evgeniya", "Vitaliy", "Eugene"]

def find_switcher(user_list: list) -> str:
    switcher = "Mykola Kuzmin"
    if switcher in user_list:
        return f"Here is the swither = **{switcher}**"
    else:
        return "There is no switcher."
print(find_switcher(my_list))

print("-" * 100) #------------------------------------------------------------------------------------------------------

switcher_info = ["Mykola", "Kuzmin"]

def my_func(users):
    return "Switcher with the name: {} and surname: {}".format(*users)

print(my_func(switcher_info))

print("-" * 100)   #------------------------------------------------------------------------------------------------------

switcher_info = ["Mykola", "Kuzmin"]

def my_func(name, surname):
    return f"Switcher with the name: {name} and surname: {surname}"

print(my_func(*switcher_info))

print("-" * 100)   #------------------------------------------------------------------------------------------------------


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

list1 = list("hello")
for i in range(len(list1)):
    print(f"{i} : {list1[i]}")
#----------------------------------------------------
s = '\nHello World'
i = 0
while i < len(s):
    print(s[i:i + 1], '', end= '')
    i += 1
#----------------------------------------------------
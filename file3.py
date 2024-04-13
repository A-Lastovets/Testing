fruits = ["banana", "orange", "apple"]
prices = [10, 20, 30]

for name in fruits:
    for cost in prices:
        print(name + ':', cost)

# for name, cost in zip(fruits, prices):
#     print(name + ':', cost)

# i = 0
# while i < len(fruits):
#     print(fruits[i] + ':', prices[i])
#     i += 1

# for index, value in enumerate(prices):
#     print(index, value)

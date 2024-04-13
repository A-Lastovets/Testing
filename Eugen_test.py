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


n = int(input('Enter number of last range: '))
s = 0
i = 1
while i <= n:
    s = i + s
    i += 1
print(f'Sum below numbers 1 to {n}: ', s)


# n = int(input('Enter number of last range: '))
# print(f'Sum below numbers 1 to {n}: ', int((n * (n + 1)) / 2), end =' ')

#--------------------------------------------------------


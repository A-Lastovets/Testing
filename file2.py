# Дано два списка:
# first_list = [1, 6, 7, 9, 2, 3, 4]
# second_list = [5, 2, 1, 8, 3, 7, 10]
# Вывести:
# 1) элементы с первого списка, которых нет во втором
# 2) элементы со второго списка, которых нет в первом
#-----------------------------------------------------------------
# first method :
# first_list = set([1, 6, 7, 9, 2, 3, 4])
# second_list = set([5, 2, 1, 8, 3, 7, 10])
# print(set(first_list) - set(second_list))
# print(set(second_list) - set(first_list))
# or 
# print(set(first_list).difference(second_list))
# print(set(second_list).difference(first_list))
#-----------------------------------------------------------------
# second method :
# first_list2 = []
# second_list2 =[]
# for element in first_list1 and second_list1:
#     if element not in second_list1:
#         first_list2.append(element)
# print("Elements of list1 that are not in list2: ", first_list2)
# for element in second_list1:
#     if element not in first_list1:
#         second_list2.append(element)
# print("Elements of list2 that are not in list1: ", second_list2)
#------------------------------------------------------------------
# другие примеры работы с множеством

text = input("Enter text : \n")                                      # просим ввести текст
first_set = set()                                                    # преобразовываем в множество новый список
while text != "":                                                    # если ничего не вводить и нажать Enter - выход с программы
    words = text.split()                                             # метод  "split" преобразовывает текст в список
    first_set.update(words)                                          # добавляем эти слова в множество
    text = input("Enter text : \n")                                  # повторный вызов ввести текст для добавления новых слов в множество
print(first_set)                                                     # вывод множества
print("Number of words in the text:", len(first_set))                # вывод количества слов в множестве
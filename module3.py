# print("-" * 100)

# import datetime
# now = datetime.datetime.now()
# print(now)
# print("-" * 100)
# # from datetime import datetime

# # current_datetime = datetime.now()

# # print(current_datetime.year)
# # print(current_datetime.month)
# # print(current_datetime.day)
# # print(current_datetime.hour)
# # print(current_datetime.minute)
# # print(current_datetime.second)
# # print(current_datetime.microsecond)
# # print(current_datetime.tzinfo)

# from datetime import datetime

# current_datetime = datetime.now()
# print(current_datetime.date())
# print(current_datetime.time())

# print("-" * 100)

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні {day_of_week} день тижня")  

from datetime import datetime, timedelta

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

from datetime import datetime

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)



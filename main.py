import time
name, surname = input(), input()
seconds = time.time()
local_time = time.ctime(seconds)
currentHour = int(local_time[11:13])
z = []
if 0 <= currentHour <= 5:
    z = "Доброй ночи"
elif 6 <= currentHour <= 11:
    z = "Доброе утро"
elif 12 <= currentHour <= 17:
    z = "Добрый день"
elif 18 <= currentHour <= 23:
    z = "Добрый вечер"
print(z, "дорогой", name.upper()[0] + name.lower()[1:], surname.upper()[0] + surname.lower()[1:])

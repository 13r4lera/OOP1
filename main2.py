from datetime import datetime

from task2 import People

p = People()

for i in range(int(input("Количество людей:"))):
    surname = input("Фамилия: ")
    name = input("Имя: ")
    phone = input("Телефон: ")
    birthday = datetime.strptime(input("Дата рождения (дд.мм.гггг): "), "%d.%m.%Y").date()
    p.add(surname, name, phone, birthday)

p.show(int(input("Месяц для поиска: ")))
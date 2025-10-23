groupmates = [
    {
        "name": "Денис",
        "surname": "Чуенко",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Александр",
        "surname": "Поленов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Сергей",
        "surname": "Тетов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Константин",
        "surname": "Базаров",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 2, 2]
    },
    {
        "name": "Кирилл",
        "surname": "Купава",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 4, 5]
    },
]

avg_score = float(input("Введите значение "))

def avg_calc(marks):
    score = 0.0
    for mark in marks:
        score += mark

    score = score / len(marks)
    return score

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Оценки".ljust(20), u"Среднее значение".ljust(20))
    for student in students:
        M = avg_calc(student['marks'])
        if M > avg_score:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["marks"]).ljust(20), str(M).ljust(20))

print_students(groupmates)
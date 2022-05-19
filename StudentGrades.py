grades = []


def display_grades():
    print(grades)


def add_grades():
    grade = 0
    while grade != -1:
        grade = int(input("Enter grade: "))
        grades.append(grade)
        if grade == -1:
            del grades[len(grades) - 1]
            break


def get_average_grade():
    sum = 0
    for i in grades:
        sum += i
    return sum / len(grades)


def round_up_grades():
    for i in range(len(grades)):
        if grades[i] == 69 or grades[i] == 79 or grades[i] == 89:
            grades[i] += 1
    return grades


def remove_low_grade():
    low = grades[0]
    for i in grades:
        if i < low:
            low = i
    grades.remove(low)


add_grades()
round_up_grades()
remove_low_grade()
display_grades()
print("Average: " + str(get_average_grade()))

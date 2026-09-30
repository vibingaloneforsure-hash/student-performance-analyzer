def calculate_result(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    return total, average, grade, result
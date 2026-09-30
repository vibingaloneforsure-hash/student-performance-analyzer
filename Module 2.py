
def add_student():
    name = input("Enter student name: ")

    m1 = float(input("Enter M1 marks: "))
    m2 = float(input("Enter M2 marks: "))
    m3 = float(input("Enter M3 marks: "))

    total, average, grade, result = calculate_result(m1, m2, m3)

    student = {
        "name": name,
        "m1": m1,
        "m2": m2,
        "m3": m3,
        "total": total,
        "average": average,
        "grade": grade,
        "result": result
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Total   :", total)
    print("Average :", f"{average:.2f}")
    print("Grade   :", grade)
    print("Result  :", result)
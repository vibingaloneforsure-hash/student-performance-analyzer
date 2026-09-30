students = []


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


def display_students():
    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 90)
    print(f"{'Name':<15}{'M1':<8}{'M2':<8}{'M3':<8}"
          f"{'Total':<10}{'Average':<10}{'Grade':<8}{'Result'}")
    print("=" * 90)

    for student in students:
        print(f"{student['name']:<15}"
              f"{student['m1']:<8.0f}"
              f"{student['m2']:<8.0f}"
              f"{student['m3']:<8.0f}"
              f"{student['total']:<10.0f}"
              f"{student['average']:<10.2f}"
              f"{student['grade']:<8}"
              f"{student['result']}")

    print("=" * 90)


def find_topper():
    if len(students) == 0:
        print("\nNo student records found.")
        return

    topper = students[0]

    for student in students:
        if student["average"] > topper["average"]:
            topper = student

    print("\nTOPPER")
    print("-" * 30)
    print("Name    :", topper["name"])
    print("Total   :", topper["total"])
    print("Average :", f"{topper['average']:.2f}")
    print("Grade   :", topper["grade"])


def search_student():
    name = input("\nEnter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print("-" * 30)
            print("Name    :", student["name"])
            print("M1      :", student["m1"])
            print("M2      :", student["m2"])
            print("M3      :", student["m3"])
            print("Total   :", student["total"])
            print("Average :", f"{student['average']:.2f}")
            print("Grade   :", student["grade"])
            print("Result  :", student["result"])

            found = True
            break

    if not found:
        print("\nStudent not found.")


def class_statistics():
    if len(students) == 0:
        print("\nNo student records found.")
        return

    total_students = len(students)
    passed = 0
    failed = 0
    total_average = 0

    for student in students:
        total_average += student["average"]

        if student["result"] == "PASS":
            passed += 1
        else:
            failed += 1

    class_average = total_average / total_students
    pass_percentage = (passed / total_students) * 100

    print("\nCLASS STATISTICS")
    print("-" * 35)
    print("Total Students :", total_students)
    print("Passed         :", passed)
    print("Failed         :", failed)
    print("Class Average  :", f"{class_average:.2f}")
    print("Pass Percentage:", f"{pass_percentage:.2f}%")


def main():
    while True:
        print("\n" + "=" * 45)
        print("       STUDENT PERFORMANCE ANALYZER")
        print("=" * 45)

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Find Topper")
        print("4. Search Student")
        print("5. Class Statistics")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            find_topper()

        elif choice == "4":
            search_student()

        elif choice == "5":
            class_statistics()

        elif choice == "6":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()
def search_student(students):
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
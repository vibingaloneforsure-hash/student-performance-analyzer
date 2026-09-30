def class_statistics(students):
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
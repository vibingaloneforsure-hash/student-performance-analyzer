def display_students(students):
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
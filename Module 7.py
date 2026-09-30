from student import students, add_student
from display import display_students
from topper import find_topper
from search import search_student
from statistics import class_statistics


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
            display_students(students)

        elif choice == "3":
            find_topper(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            class_statistics(students)

        elif choice == "6":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()
Problem Statement

Student Performance Analyzer

Managing and analyzing marks of multiple students manually can be time-consuming. A simple computerized system can make this process easier and more organized.

The Student Performance Analyzer is a Python program designed to store student information and analyze academic performance based on marks in three subjects: M1, M2, and M3.

For every student, the program calculates the total marks and average marks. It then assigns a grade based on the average and determines whether the student has passed or failed.

A student passes only when they obtain at least 40 marks in all three subjects.

The system also provides options to display all student records, find the topper, search for a particular student, and calculate class statistics.

Input

The program accepts:

• Student name
• M1 marks
• M2 marks
• M3 marks

Processing

Total

Total = M1 + M2 + M3

Average

Average = Total / 3

Grade

The grade is assigned according to the calculated average.

Result

The student is marked PASS when:

M1 >= 40 AND M2 >= 40 AND M3 >= 40

Otherwise:

FAIL

Output

The program provides:

• Individual student performance
• All student records
• Topper information
• Student search results
• Class statistics
• Pass percentage

Programming Concepts Used

• Variables
• Input and output
• Functions
• Lists
• Dictionaries
• Conditional statements
• Loops
• String formatting
• Menu-driven programming

Purpose

The purpose of this project is to demonstrate how basic Python programming concepts can be combined to create a practical student performance management application.

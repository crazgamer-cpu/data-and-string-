student_marks = {"Alice": 85, "Bob": 90,"Charlie": 78, "David": 92, "Eva": 88}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")


numbers = list(range(1, 11))
first_five = numbers[:5]
reversed_first_five = first_five[::-1]
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_first_five)

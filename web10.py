
Skip to main content





















Personal
A..prasannakumar

Upgrade

Auto



University Scholarship Allocation: Design a system that evaluates applicants using aggregate marks, subject-wise minimum scores, attendance, and income criteria, ranks eligible students, and resolves ties using predefined rules. write a code in python 
Here's a Python program for a University Scholarship Allocation System that:

Checks aggregate marks
Verifies subject-wise minimum scores
Checks attendance percentage
Verifies family income criteria
Ranks eligible students
Resolves ties using predefined rules:
Higher aggregate marks
Higher attendance
Lower family income
Alphabetical order of name


# University Scholarship Allocation System
 
class Student:
    def __init__(self, name, marks, attendance, income):
        self.name = name
        self.marks = marks  # Dictionary of subject marks
        self.attendance = attendance
        self.income = income
 
    def aggregate(self):
        return sum(self.marks.values()) / len(self.marks)
 
    def is_eligible(self):
        MIN_SUBJECT_MARK = 50
        MIN_AGGREGATE = 70
        MIN_ATTENDANCE = 75
        MAX_INCOME = 300000
 
        # Check subject-wise minimum marks
        for mark in self.marks.values():
            if mark < MIN_SUBJECT_MARK:
                return False
 
        # Check aggregate
        if self.aggregate() < MIN_AGGREGATE:
            return False
 
        # Check attendance
        if self.attendance < MIN_ATTENDANCE:
            return False
 
        # Check income
        if self.income > MAX_INCOME:
            return False
 
        return True
 
 
# Sample Student Data
students = [
    Student("Amit", {"Math": 85, "Physics": 78, "Chemistry": 80}, 90, 250000),
    Student("Bhavna", {"Math": 88, "Physics": 82, "Chemistry": 84}, 88, 220000),
    Student("Charan", {"Math": 75, "Physics": 70, "Chemistry": 72}, 80, 280000),
    Student("Deepa", {"Math": 88, "Physics": 82, "Chemistry": 84}, 92, 220000),
    Student("Farhan", {"Math": 45, "Physics": 85, "Chemistry": 80}, 90, 200000)
]
 
# Filter eligible students
eligible_students = [student for student in students if student.is_eligible()]
 
# Rank students with tie-breaking rules
eligible_students.sort(
    key=lambda s: (
        -s.aggregate(),      # Higher aggregate first
        -s.attendance,       # Higher attendance first
        s.income,            # Lower income first
        s.name               # Alphabetical order
    )
)
 
# Display Results
print("=== Scholarship Ranking List ===\n")
 
for rank, student in enumerate(eligible_students, start=1):
    print(f"Rank {rank}")
    print(f"Name       : {student.name}")
    print(f"Aggregate  : {student.aggregate():.2f}%")
    print(f"Attendance : {student.attendance}%")
    print(f"Income     : ₹{student.income}")
    print("-" * 35)
Sample Output
=== Scholarship Ranking List ===

Rank 1
Name       : Deepa
Aggregate  : 84.67%
Attendance : 92%
Income     : ₹220000
-----------------------------------

Rank 2
Name       : Bhavna
Aggregate  : 84.67%
Attendance : 88%
Income     : ₹220000
-----------------------------------

Rank 3
Name       : Amit
Aggregate  : 81.00%
Attendance : 90%
Income     : ₹250000
-----------------------------------

Rank 4
Name       : Charan
Aggregate  : 72.33%
Attendance : 80%
Income     : ₹280000
-----------------------------------
Time Complexity: O(n log n) due to sorting, where n is the number of applicants.

Explore more offers
Sponsored



Python programming - Step-By-Step Tutorials
www.udemy.com/Course/Python
Be able to use Python for Data Science and Machine Learning. Sign up now! We empower organizations and individuals with flexible and effective skill development.

Python for Everybody - Coursera - Python for Beginners
www.coursera.org/python
Learn Python programming with a beginner-friendly course on Coursera. ₹1699 for expert-led, career-boosting courses. Enroll today.






Add user input and validation

Make the criteria configurable

Export the ranked list to CSV



Message Copilot

AI-generated content may be incorrect


# University Academic Progression Audit System

# Student details
student_name = "Ravi"

# Semester marks: subject name and marks obtained
semester_marks = {
    "Mathematics": 75,
    "Python Programming": 82,
    "Physics": 35,
    "English": 68
}

# Minimum passing marks for each subject
pass_marks = 40

# Attendance percentage
attendance = 78
minimum_attendance = 75

# Prerequisite completion status
prerequisites = {
    "Programming Fundamentals": True,
    "Basic Mathematics": True,
    "Computer Fundamentals": False
}

# Audit process
print("UNIVERSITY ACADEMIC PROGRESSION AUDIT")
print("=" * 45)
print("Student Name:", student_name)

outstanding = []

# 1. Check subject pass conditions
print("\n1. SEMESTER MARKS AUDIT")

for subject, marks in semester_marks.items():
    if marks >= pass_marks:
        print(subject, ":", marks, "- PASS")
    else:
        print(subject, ":", marks, "- FAIL")
        outstanding.append(
            f"Pass {subject} (minimum {pass_marks} marks required)"
        )

# 2. Check attendance
print("\n2. ATTENDANCE AUDIT")
print("Attendance:", attendance, "%")

if attendance >= minimum_attendance:
    print("Attendance requirement: SATISFIED")
else:
    print("Attendance requirement: NOT SATISFIED")
    outstanding.append(
        f"Meet minimum attendance of {minimum_attendance}%"
    )

# 3. Check prerequisites
print("\n3. PREREQUISITE AUDIT")

for prerequisite, completed in prerequisites.items():
    if completed:
        print(prerequisite, "- COMPLETED")
    else:
        print(prerequisite, "- NOT COMPLETED")
        outstanding.append(
            f"Complete prerequisite: {prerequisite}"
        )

# 4. Final progression decision
print("\n4. FINAL PROGRESSION DECISION")
print("-" * 45)

if len(outstanding) == 0:
    print("Status: ELIGIBLE FOR NEXT SEMESTER")
    print("All academic requirements are satisfied.")
else:
    print("Status: NOT ELIGIBLE FOR PROGRESSION")
    print("\nOutstanding Requirements:")

    for i, requirement in enumerate(outstanding, start=1):
        print(f"{i}. {requirement}")

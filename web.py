# University Scholarship Allocation System

MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 60
MIN_ATTENDANCE = 75
MAX_FAMILY_INCOME = 2502000

students = [
    {
        "name": "Ravi",
        "marks": [85, 90, 80, 88],
        "attendance": 90,
        "income": 150000
    },
    {
        "name": "Priya",
        "marks": [90, 95, 85, 92],
        "attendance": 95,
        "income": 200000
    },
    {
        "name": "Arun",
        "marks": [80, 55, 85, 90],
        "attendance": 92,
        "income": 120000
    },
    {
        "name": "Sita",
        "marks": [85, 90, 80, 88],
        "attendance": 90,
        "income": 100000
    },
    {
        "name": "Kiran",
        "marks": [78, 82, 80, 85],
        "attendance": 70,
        "income": 90000
    }
]

eligible_students = []

for student in students:
    marks = student["marks"]
    aggregate = sum(marks) / len(marks)

    if (
        aggregate >= MIN_AGGREGATE
        and all(m >= MIN_SUBJECT_MARKS for m in marks)
        and student["attendance"] >= MIN_ATTENDANCE
        and student["income"] <= MAX_FAMILY_INCOME
    ):
        student["aggregate"] = aggregate
        eligible_students.append(student)



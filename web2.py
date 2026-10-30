# Student Timetable Conflict Detection System

# Timetable format:
# (day, start_time, end_time, room, course)

timetable = [
    ("Monday", "09:00", "10:00", "R101", "Python"),
    ("Monday", "10:00", "11:00", "R102", "Mathematics"),
    ("Monday", "09:30", "10:30", "R103", "Physics"),
    ("Tuesday", "11:00", "12:00", "R101", "English")
]

# Unavailable rooms and their time periods
unavailable_rooms = [
    ("Monday", "09:00", "11:00", "R103"),
    ("Tuesday", "11:00", "12:00", "R105")
]


def to_minutes(time):
    """Convert HH:MM string into minutes."""
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def overlaps(start1, end1, start2, end2):
    """Check whether two time periods overlap."""
    return (
        to_minutes(start1) < to_minutes(end2)
        and to_minutes(start2) < to_minutes(end1)
    )


def detect_conflicts(schedule):
    print("\n--- TIMETABLE CONFLICTS ---")

    found = False

    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            c1 = schedule[i]
            c2 = schedule[j]

            # Check overlapping classes on the same day
            if c1[0] == c2[0] and overlaps(
                c1[1], c1[2], c2[1], c2[2]
            ):
                print(
                    f"Time conflict: {c1[4]} and {c2[4]} "
                    f"on {c1[0]}"
                )
                found = True

    if not found:
        print("No overlapping classes found.")


def check_unavailable_rooms(schedule):
    print("\n--- ROOM AVAILABILITY ---")

    found = False

    for course in schedule:
        for room in unavailable_rooms:
            if (
                course[0] == room[0]
                and course[3] == room[3]
                and overlaps(
                    course[1], course[2],
                    room[1], room[2]
                )
            ):
                print(
                    f"{course[4]} cannot use room {course[3]} "
                    f"on {course[0]} "
                    f"({course[1]}-{course[2]})"
                )
                found = True

    if not found:
        print("All rooms are available.")


def validate_timetable(schedule):
    print("\n--- TIMETABLE VALIDATION ---")

    conflicts = 0
    room_issues = 0

    # Check student schedule conflicts
    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            c1 = schedule[i]
            c2 = schedule[j]

            if (
                c1[0] == c2[0]
                and overlaps(c1[1], c1[2], c2[1], c2[2])
            ):
                conflicts += 1

    # Check unavailable rooms
    for course in schedule:
        for room in unavailable_rooms:
            if (
                course[0] == room[0]
                and course[3] == room[3]
                and overlaps(
                    course[1], course[2],
                    room[1], room[2]
                )
            ):
                room_issues += 1

    if conflicts == 0 and room_issues == 0:
        print("Timetable is VALID.")
    else:
        print("Timetable is INVALID.")
        print("Schedule conflicts:", conflicts)
        print("Room availability issues:", room_issues)


# Example of a schedule represented by a string
schedule_text = "Monday,09:00,10:00,R101,Python"
print("Example schedule string:", schedule_text)

# Convert the string into a tuple
course_tuple = tuple(schedule_text.split(","))
print("Converted schedule tuple:", course_tuple)

# Run the system
detect_conflicts(timetable)
check_unavailable_rooms(timetable)
validate_timetable(timetable)

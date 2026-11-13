# Placement Readiness Tracker
# Task 1: store students as a list of dictionaries

students = [
    {"name": "Manas",  "roll_no": 101, "aptitude": 78, "verbal": 65, "coding": 88},
    {"name": "Danav",   "roll_no": 102, "aptitude": 92, "verbal": 85, "coding": 90},
    {"name": "Kabir",  "roll_no": 103, "aptitude": 45, "verbal": 38, "coding": 30},
    {"name": "Meera",  "roll_no": 104, "aptitude": 60, "verbal": 72, "coding": 55},
    {"name": "Rohan",  "roll_no": 105, "aptitude": 35, "verbal": 40, "coding": 28},
]

# Task 1: add one more student through input()
print("--- Add a new student ---")
name = input("Enter name: ")
roll_no = int(input("Enter roll number: "))        # convert str -> int

new_student = {"name": name, "roll_no": roll_no}

for subject in ["aptitude", "verbal", "coding"]:
    while True:                                     # loop rejects invalid scores
        score = int(input(f"Enter {subject} score (0-100): "))
        if 0 <= score <= 100:
            break
        print("Invalid! Score must be between 0 and 100.")
    new_student[subject] = score

students.append(new_student)


# Task 2: functions
def average(student):
    """Return the mean of the three scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Return grade based on average."""
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"
    
def top_scorer(students):
    """Return the student with the highest average."""
    return max(students, key=average)


def needs_practice(students, limit=40):
    """Return students whose average is below limit (default 40)."""
    return [s for s in students if average(s) < limit]

# Task 2: formatted result table
print("\n" + "=" * 64)
print(f"{'Roll':<6}{'Name':<12}{'Apt':>5}{'Verb':>6}{'Code':>6}{'Avg':>8}   Grade")
print("=" * 64)
for s in students:
    avg = average(s)
    print(f"{s['roll_no']:<6}{s['name']:<12}{s['aptitude']:>5}{s['verbal']:>6}"
          f"{s['coding']:>6}{avg:>8.2f}   {grade(avg)}")
print("=" * 64)

best = top_scorer(students)
print(f"\nTop scorer: {best['name']} (average {average(best):.2f})")

print("\nStudents needing extra practice:")
for s in needs_practice(students):
    print(f"  - {s['name']} (average {average(s):.2f})")
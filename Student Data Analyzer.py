print("Student Data Analyzer")

marks = []

try:
    n = int(input("Enter number of students: "))
except:
    print("Invalid input")
    exit()

if n <= 0:
    print("Invalid number")
    exit()

for i in range(n):
    try:
        m = int(input(f"Enter marks of student {i+1}: "))
    except:
        print("Invalid input")
        exit()

    if m < 0 or m > 100:
        print("Marks should be between 0 and 100")
        exit()

    marks.append(m)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed = sum(1 for m in marks if m >= 33)
failed = len(marks) - passed

print("\n--- Analysis ---")
print("Marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)

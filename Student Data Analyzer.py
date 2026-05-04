print("Student Data Analyzer")

marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)

average = sum(marks) / len(marks)

highest = max(marks)
lowest = min(marks)

print("\n--- Analysis ---")
print("Marks:", marks)
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)
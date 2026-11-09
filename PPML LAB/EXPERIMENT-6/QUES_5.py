import csv

with open("student.csv", "w", newline="") as f:
    w = csv.writer(f)

    w.writerow(["Roll No", "Name", "Marks"])
    w.writerow([1, "Rahul", 85])
    w.writerow([2, "Amit", 90])
    w.writerow([3, "Ravi", 80])

with open("student.csv", "r") as f:
    r = csv.reader(f)

    print("Student Details:")

    for row in r:
        print(row)
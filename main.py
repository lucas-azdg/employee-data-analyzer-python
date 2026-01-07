import csv

employees = []

with open("employees.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        employee = {
            "name": row["name"],
            "department": row["department"],
            "salary": int(row["salary"]),
            "absent_days": int(row["absent_days"])
        }
        employees.append(employee)

# --- MÉTRICAS ---

total_salary = sum(emp["salary"] for emp in employees)
average_salary = total_salary / len(employees)

total_absent_days = sum(emp["absent_days"] for emp in employees)
average_absence = total_absent_days / len(employees)

print("Total employees:", len(employees))
print("Average salary:", average_salary)
print("Total absent days:", total_absent_days)
print("Average absence per employee:", average_absence)





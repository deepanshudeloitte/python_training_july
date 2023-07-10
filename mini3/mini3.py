employees = [
    {"name": "test_1", "age": 30, "salary": 50000},
    {"name": "test_2", "age": 67, "salary": 60000},
    {"name": "test_3", "age": 35, "salary": 70000},

]

# lambda expression to convert salary to hourly wage
convert_to_hourly = lambda emp: {**emp, "salary": round(emp["salary"] / 2080, 2)}

# map() to transform the salary of each employee
employees = list(map(convert_to_hourly, employees))

#  expression to determine employment status
get_employment_status = lambda emp: {**emp, "status": "Junior" if emp["age"] < 30 else "Senior"}

# map() to add employment status to each employee dictionary
employees = list(map(get_employment_status, employees))

# Print the transformed dataset
for emp in employees:
    print(emp)


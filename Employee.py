import json


class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state


def getEmployeeDetails(emp):
    return [emp.name, emp.dob, emp.height, emp.city, emp.state]


def read_employees(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    employeeObjects = []
    employeeDetails = []
    for employee in data:
        emp = Employee(
            employee["Name"],
            employee["DOB"],
            employee["Height"],
            employee["City"],
            employee["State"],
        )
        employeeObjects.append(emp)
        employeeDetails.append(getEmployeeDetails(emp))
    print(employeeDetails)  # Printing employees list for reference
    f.close()
    return employeeObjects


employees = read_employees("_1_variable_and_datatypes\_2_operator_\json_&_OOP\employee.json")
print(list(employees))
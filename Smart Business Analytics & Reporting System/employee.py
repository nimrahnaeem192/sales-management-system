import csv
import os
import re


class Employee:

    def __init__(self):
        self.file = "employees.csv"



    def load_employees(self):

        employees = []

        if os.path.exists(self.file):

            with open(self.file, "r", newline="") as f:

                reader = csv.DictReader(f)

                for row in reader:
                    employees.append(row)

        else:

            with open(self.file, "w", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    "EmployeeID",
                    "EmployeeName",
                    "EmployeePhone",
                    "Department",
                    "Salary"
                ])

        return employees




    def save_employees(self, employees):

        with open(self.file, "w", newline="") as f:

            fields = [
                "EmployeeID",
                "EmployeeName",
                "EmployeePhone",
                "Department",
                "Salary"
            ]

            writer = csv.DictWriter(f, fieldnames=fields)

            writer.writeheader()

            writer.writerows(employees)



    def generate_id(self):

        employees = self.load_employees()

        if not employees:
            return 1001

        ids = []

        for employee in employees:
            ids.append(int(employee["EmployeeID"]))

        return max(ids) + 1



    def add_employee(self):

        employees = self.load_employees()

        name = input("Enter Employee Name: ")

        while True:

            phone = input("Enter Employee Phone Number: ")

            check = re.fullmatch(r"03\d{9}", phone)

            if check:
                break

            else:
                print("Invalid Phone Number")

        department = input("Enter Department: ")

        salary = int(input("Enter Salary: "))

        employee = {

            "EmployeeID": self.generate_id(),
            "EmployeeName": name,
            "EmployeePhone": phone,
            "Department": department,
            "Salary": salary

        }

        employees.append(employee)

        self.save_employees(employees)

        print("Employee Added Successfully")




    def search_employee(self):

        employees = self.load_employees()

        search_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:

            if employee["EmployeeID"] == search_id:

                found = True

                print(employee)

        if not found:

            print("Employee Not Found")



    def update_employee(self):

        employees = self.load_employees()

        update_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:

            if employee["EmployeeID"] == update_id:

                found = True

                employee["EmployeeName"] = input("Enter New Name: ")
                employee["EmployeePhone"] = int(input("Enter New Phone: "))
                employee["Department"] = input("Enter New Department: ")
                employee["Salary"] = input("Enter New Salary: ")

                break

        if found:

            self.save_employees(employees)

            print("Employee Updated Successfully")

        else:

            print("Employee Not Found")



    def delete_employee(self):

        employees = self.load_employees()

        delete_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:

            if employee["EmployeeID"] == delete_id:

                employees.remove(employee)

                found = True

                break

        if found:

            self.save_employees(employees)

            print("Employee Deleted Successfully")

        else:

            print("Employee Not Found")



    def view_employees(self):

        employees = self.load_employees()

        if not employees:

            print("No Employees Found")

        else:

            for employee in employees:

                print(employee)
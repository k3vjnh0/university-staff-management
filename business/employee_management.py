from typing import List
import csv
import entity.employee
import entity.staff
import entity.teacher
import entity.EDegree
import entity.EPosition
import business.allowance_calculator


class Employee_Management:
    def __init__(self):
        self.lst_emp: List[entity.employee.Employee] = []

    def add_employee(self, employee: entity.employee.Employee):
        self.lst_emp.append(employee)

    def search_by_name(self, name: str):
        result = []

        for emp in self.lst_emp:
            if name.lower() in emp.get_full_name().lower():
                result.append(emp)

        return result

    def search_by_dept(self, dept: str):
        result = []

        for emp in self.lst_emp:
            if isinstance(emp, entity.staff.Staff):
                if dept.lower() in emp.get_department().lower():
                    result.append(emp)

            if isinstance(emp, entity.teacher.Teacher):
                if dept.lower() in emp.get_faculty().lower():
                    result.append(emp)

        return result

    def list_all(self) -> List[entity.employee.Employee]:
        self.lst_emp.sort(key=lambda x: x.get_full_name())
        return self.lst_emp

    def save(self, employee: entity.employee.Employee, filename: str):
        with open(filename, "a", newline="") as data:
            writer = csv.writer(data)

            if isinstance(employee, entity.staff.Staff):
                writer.writerow(f"Staff,{employee}".split(","))

            if isinstance(employee, entity.teacher.Teacher):
                writer.writerow(f"Teacher,{employee}".split(","))

    def load(self, filename: str):
        with open(filename, "r") as f:
            lines = f.read().strip().split("\n")
            for line in lines:
                arr = line.strip().split(",")
                if arr[0].lower() == "Staff".lower():
                    s = entity.staff.Staff()
                    s.set_full_name(arr[1])
                    s.set_department(arr[2])
                    if arr[3].lower() == "HEAD".lower():
                        s.set_position(entity.EPosition.Position(1).name)
                    if arr[3].lower() == "VICE_HEAD".lower():
                        s.set_position(entity.EPosition.Position(2).name)
                    if arr[3].lower() == "STAFF".lower():
                        s.set_position(entity.EPosition.Position(3).name)
                    s.set_salary_ratio(float(arr[4]))
                    s.set_allowance(
                        business.allowance_calculator.calculate_allowance(s)
                    )
                    s.set_working_days(float(arr[6]))
                    self.lst_emp.append(s)

                if arr[0].lower() == "Teacher".lower():
                    t = entity.teacher.Teacher()
                    t.set_full_name(arr[1])
                    t.set_faculty(arr[2])
                    if arr[3].lower() == "BACHELOR".lower():
                        t.set_degree(entity.EDegree.Degree(1).name)
                    if arr[3].lower() == "MASTER".lower():
                        t.set_degree(entity.EDegree.Degree(2).name)
                    if arr[3].lower() == "DOCTOR".lower():
                        t.set_degree(entity.EDegree.Degree(3).name)
                    t.set_salary_ratio(float(arr[4]))
                    t.set_allowance(
                        business.allowance_calculator.calculate_allowance(t)
                    )
                    t.set_teaching_hours(float(arr[6]))
                    self.lst_emp.append(t)

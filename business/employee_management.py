from typing import List
import csv
import entity.employee as e
import entity.staff as s
import entity.teacher as t
import entity.EDegree as deg
import entity.EPosition as pos
import business.allowance_calculator as calc


class Employee_Management:
    def __init__(self):
        self.lst_emp: List[e.Employee] = []

    def add_employee(self, employee: e.Employee):
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
            if isinstance(emp, s.Staff):
                if dept.lower() in emp.get_department().lower():
                    result.append(emp)

            if isinstance(emp, t.Teacher):
                if dept.lower() in emp.get_faculty().lower():
                    result.append(emp)

        return result

    def list_all(self):
        self.lst_emp.sort(key=lambda x: x.get_full_name())
        return self.lst_emp

    def save(self, employee: e.Employee, filename: str):
        with open(filename, "a", newline="") as data:
            writer = csv.writer(data)

            if isinstance(employee, s.Staff):
                writer.writerow(f"Staff,{employee}".split(","))

            if isinstance(employee, t.Teacher):
                writer.writerow(f"Teacher,{employee}".split(","))

    def load(self, filename: str):
        with open(filename, "r") as f:
            lines = f.read().strip().split("\n")
            for line in lines:
                arr = line.strip().split(",")
                if arr[0] == "Staff":
                    staff = s.Staff()
                    staff.set_full_name(arr[1])
                    staff.set_department(arr[2])
                    if arr[3].lower() == "HEAD".lower():
                        staff.set_position(pos.Position(1).name)
                    if arr[3].lower() == "VICE_HEAD".lower():
                        staff.set_position(pos.Position(2).name)
                    if arr[3].lower() == "STAFF".lower():
                        staff.set_position(pos.Position(3).name)
                    staff.set_salary_ratio(float(arr[4]))
                    staff.set_allowance(calc.calculate_allowance(staff))
                    staff.set_working_days(float(arr[6]))
                    self.lst_emp.append(staff)

                if arr[0] == "Teacher":
                    teacher = t.Teacher()
                    teacher.set_full_name(arr[1])
                    teacher.set_faculty(arr[2])
                    if arr[3].lower() == "BACHELOR".lower():
                        teacher.set_degree(deg.Degree(1).name)
                    if arr[3].lower() == "MASTER".lower():
                        teacher.set_degree(deg.Degree(2).name)
                    if arr[3].lower() == "DOCTOR".lower():
                        teacher.set_degree(deg.Degree(3).name)
                    teacher.set_salary_ratio(float(arr[4]))
                    teacher.set_allowance(calc.calculate_allowance(teacher))
                    teacher.set_teaching_hours(float(arr[6]))
                    self.lst_emp.append(teacher)

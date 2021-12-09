from typing import List
import csv
import entity.employee
import entity.staff
import entity.teacher
import entity.EDegree
import entity.EPosition
import business.allowance_calculator

Employee = entity.employee.Employee
Staff = entity.staff.Staff
Teacher = entity.teacher.Teacher
Degree = entity.EDegree.Degree
Position = entity.EPosition.Position
calculate_allowance = business.allowance_calculator.calculate_allowance


class Employee_Management:
    def __init__(self):
        self.lst_emp: List[Employee] = []

    def add_employee(self, employee: Employee):
        self.lst_emp.append(employee)

    def search_by_name(self, name: str):
        result = []

        for emp in self.lst_emp:
            if emp.get_full_name().lower() == name.lower():
                result.append(emp)

        return result

    def search_by_dept(self, dept: str):
        result = []

        for emp in self.lst_emp:
            if isinstance(emp, Staff):
                if emp.get_department().lower() == dept.lower():
                    result.append(emp)

            if isinstance(emp, Teacher):
                if emp.get_faculty().lower() == dept.lower():
                    result.append(emp)

        return result

    def list_all(self):
        return self.lst_emp.sort(key=lambda x: x.get_full_name())

    def save(self, employee: Employee, filename: str):
        with open(filename, "w", newline="\n") as data:
            writer = csv.writer(data)

            if isinstance(employee, Staff):
                writer.writerow(f"Staff, {employee}")

            if isinstance(employee, Teacher):
                writer.writerow(f"Teacher, {employee}")

    def load(self, filename: str):
        with open(filename, "r") as f:
            line = f.readline().strip().split(", ")

            if line[0].lower() == "Staff".lower():
                s = Staff()
                s.set_full_name(line[1])
                s.set_department(line[2])
                if line[3].lower() == "HEAD".lower():
                    s.set_position(Position.HEAD)
                if line[3].lower() == "VICE_HEAD".lower():
                    s.set_position(Position.VICE_HEAD)
                if line[3].lower() == "STAFF".lower():
                    s.set_position(Position.STAFF)
                s.set_salary_ratio(float(line[4]))
                s.set_allowance(calculate_allowance(s))
                s.set_working_days(float(line[6]))
                self.lst_emp.append(s)

            if line[0].lower() == "Teacher".lower():
                t = Teacher()
                t.set_full_name(line[1])
                t.set_faculty(line[2])
                if line[3].lower() == "DOCTOR".lower():
                    t.set_degree(Degree.DOCTOR)
                if line[3].lower() == "MASTER".lower():
                    t.set_degree(Degree.MASTER)
                if line[3].lower() == "BACHELOR".lower():
                    t.set_degree(Degree.BACHELOR)
                t.set_salary_ratio(float(line[4]))
                t.set_allowance(calculate_allowance(t))
                t.set_teaching_hours(float(line[6]))
                self.lst_emp.append(t)

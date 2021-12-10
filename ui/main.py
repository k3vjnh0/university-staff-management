from typing import List
import os
import entity.employee
import entity.staff
import entity.teacher
import entity.EDegree
import entity.EPosition
import business.allowance_calculator
import business.employee_management


def create_new_employee():
    choice = input(
        "Do you want to create a Staff or a Teacher (enter S for Staff, otherwise for Teacher)?"
    )
    if choice.lower() == "s":
        s = entity.staff.Staff()

        name = input("Name: ")
        s.set_full_name(name)

        while True:
            try:
                salary_ratio = input("Salary ratio: ")
                s.set_salary_ratio(float(salary_ratio))
                break
            except ValueError:
                print("Your input is invalid. Number is recommended.")

        faculty = input("Department: ")
        s.set_department(faculty)

        while True:
            try:
                degree = input("Position (1=HEAD; 2=VICE HEAD; 3=STAFF): ")
                if degree == "1":
                    s.set_position(entity.EPosition.Position(1).name)
                    break
                elif degree == "2":
                    s.set_position(entity.EPosition.Position(2).name)
                    break
                elif degree == "3":
                    s.set_position(entity.EPosition.Position(3).name)
                    break
                else:
                    continue
            except ValueError:
                print("Your input is invalid. Please select 1, 2 or 3.")

        while True:
            try:
                teaching_hours = input("Number of working days: ")
                s.set_working_days(float(teaching_hours))
                break
            except ValueError:
                print("Your input is invalid. Number is recommended.")

        return s

    else:
        t = entity.teacher.Teacher()

        name = input("Name: ")
        t.set_full_name(name)

        while True:
            try:
                salary_ratio = input("Salary ratio: ")
                t.set_salary_ratio(float(salary_ratio))
                break
            except ValueError:
                print("Your input is invalid. Number is recommended.")

        faculty = input("Faculty: ")
        t.set_faculty(faculty)

        while True:
            try:
                degree = input("Degree (1=BACHELOR; 2=MASTER; 3=DOCTOR): ")
                if degree == "1":
                    t.set_degree(entity.EDegree.Degree(1).name)
                    break
                elif degree == "2":
                    t.set_degree(entity.EDegree.Degree(2).name)
                    break
                elif degree == "3":
                    t.set_degree(entity.EDegree.Degree(3).name)
                    break
                else:
                    continue
            except ValueError:
                print("Your input is invalid. Please select 1, 2 or 3.")

        while True:
            try:
                teaching_hours = input("Number of teaching hours: ")
                t.set_teaching_hours(float(teaching_hours))
                break
            except ValueError:
                print("Your input is invalid. Number is recommended.")

        return t


def display(lst_emp: List[entity.employee.Employee]):
    print(
        "+---------------------+----------------+-----------+-----------+----------------+----------------+----------------+"
    )
    print(
        "| %-20s| %-15s| %-10s| %-10s| %-15s| %-15s| %-15s|"
        % (
            "Name",
            "Fac/Dept",
            "Deg/Pos",
            "Sal.Rat.",
            "Allowance ($)",
            "T.Hours/W.Days",
            "Salary ($)",
        )
    )
    print(
        "+---------------------+----------------+-----------+-----------+----------------+----------------+----------------+"
    )

    total_salary = 0
    for emp in lst_emp:
        name = emp.get_full_name()
        allowance = emp.get_allowance()
        salary_ratio = emp.get_salary_ratio()
        salary = emp.get_salary()
        total_salary += salary

        if isinstance(emp, entity.staff.Staff):
            department = emp.get_department()
            position = emp.get_position()
            working_days = emp.get_working_days()
            print(
                "| %-20s| %-15s| %-10s| %-10.2f| %-15.2f| %-15.2f| %-15.2f|"
                % (
                    name,
                    department,
                    position,
                    salary_ratio,
                    allowance,
                    working_days,
                    salary,
                )
            )

        if isinstance(emp, entity.teacher.Teacher):
            faculty = emp.get_faculty()
            degree = emp.get_degree()
            teaching_hours = emp.get_teaching_hours()
            print(
                "| %-20s| %-15s| %-10s| %-10.2f| %-15.2f| %-15.2f| %-15.2f|"
                % (
                    name,
                    faculty,
                    degree,
                    salary_ratio,
                    allowance,
                    teaching_hours,
                    salary,
                )
            )

    print(
        "+---------------------+----------------+-----------+-----------+----------------+----------------+----------------+"
    )
    print("| %-95s| %-15.2f|" % ("TOTAL", total_salary))
    print(
        "+------------------------------------------------------------------------------------------------+----------------+"
    )


def main():
    emp_man = business.employee_management.Employee_Management()
    emp_man.load("data.csv")

    while True:
        os.system("clear")
        print("University Staff Management 1.0")
        print("\t1.Add staff")
        print("\t2.Search staff by name")
        print("\t3.Search staff by department/faculty")
        print("\t4.Display all staff")
        print("\t5.Exit")
        choice = input("Select function (1,2,3,4 or 5): ")

        # Add staff/teacher
        if choice == "1":
            emp = create_new_employee()
            emp.set_allowance(business.allowance_calculator.calculate_allowance(emp))
            emp_man.add_employee(emp)
            emp_man.save(emp, "data.csv")

        # Search by name
        elif choice == "2":
            name = input("\tEnter name to search: ")
            result = emp_man.search_by_name(name)
            display(result)

        # Search by dept/fac
        elif choice == "3":
            dept = input("\tEnter dept/fac to search: ")
            result = emp_man.search_by_dept(dept)
            display(result)

        # Display staff/teacher
        elif choice == "4":
            lst_emp = emp_man.list_all()
            display(lst_emp)

        # Exit
        elif choice == "5":
            break

        else:
            continue

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()

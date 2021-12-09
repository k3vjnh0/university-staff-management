# from employee import Employee
# from allowance_calculator import calculate_allowance
import employee
import allowance_calculator

Employee = employee.Employee
calculate_allowance = allowance_calculator.calculate_allowance()


class Staff(Employee):
    def __init__(self):
        self.department = ""
        self.working_days = 0
        self.position = None
        self.allowance = calculate_allowance(self)

    def get_department(self):
        return self.department

    def set_department(self, department):
        self.department = department

    def get_working_days(self):
        return self.working_days

    def set_working_days(self, working_days):
        self.working_days = working_days

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def get_salary(self):
        return (
            self.get_salary_ratio() * 730
            + self.get_allowance()
            + self.get_working_days() * 30
        )

    def __str__(self):
        return (
            self.get_full_name()
            + ", "
            + self.get_department()
            + ", "
            + str(self.get_position())
            + ", "
            + str(self.get_salary_ratio())
            + ", "
            + str(self.get_allowance())
            + ", "
            + str(self.get_working_days())
            + ", "
            + str(self.get_salary())
        )

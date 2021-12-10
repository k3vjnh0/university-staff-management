import entity.employee as e
import entity.EDegree as deg
import business.allowance_calculator as calc


class Teacher(e.Employee):
    def __init__(self):
        self.faculty = ""
        self.teaching_hours = 0
        self.degree = deg.Degree
        self.allowance = calc.calculate_allowance(self)

    def get_faculty(self):
        return self.faculty

    def set_faculty(self, faculty):
        self.faculty = faculty

    def get_degree(self):
        return self.degree

    def set_degree(self, degree):
        self.degree = degree

    def get_teaching_hours(self):
        return self.teaching_hours

    def set_teaching_hours(self, teaching_hours):
        self.teaching_hours = teaching_hours

    def get_salary(self):
        return (
            self.get_salary_ratio() * 730
            + self.get_allowance()
            + self.get_teaching_hours() * 45
        )

    def __str__(self):
        return (
            self.get_full_name()
            + ","
            + self.get_faculty()
            + ","
            + str(self.get_degree())
            + ","
            + str(self.get_salary_ratio())
            + ","
            + str(self.get_allowance())
            + ","
            + str(self.get_teaching_hours())
            + ","
            + str(self.get_salary())
        )

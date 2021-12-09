class Employee:
    def __init__(self):
        self.full_name = ''
        self.salary_ratio = 0
        self.allowance = 0

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_salary_ratio(self):
        return self.salary_ratio

    def set_salary_ratio(self, salary_ratio):
        self.salary_ratio = salary_ratio

    def get_allowance(self):
        return self.allowance

    def set_allowance(self, allowance):
        self.allowance = allowance

    def get_salary(self):
        pass

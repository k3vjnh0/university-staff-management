import entity.staff
import entity.teacher
import entity.EDegree
import entity.EPosition

Staff = entity.staff.Staff
Teacher = entity.teacher.Teacher
Degree = entity.EDegree.Degree
Position = entity.EPosition.Position


def calculate_allowance(employee):
    allowance = 0

    if isinstance(employee, Staff):
        if employee.get_position() == Position.HEAD:
            allowance = 2000

        if employee.get_position() == Position.VICE_HEAD:
            allowance = 1000

        if employee.get_position() == Position.STAFF:
            allowance = 500

    if isinstance(employee, Teacher):
        if employee.get_degree() == Degree.BACHELOR:
            allowance = 300

        if employee.get_degree() == Degree.MASTER:
            allowance = 500

        if employee.get_degree() == Degree.DOCTOR:
            allowance = 1000

    return allowance

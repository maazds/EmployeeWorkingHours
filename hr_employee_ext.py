from odoo import api,fields,models
from datetime import date,datetime,timedelta

class HrEmployeeExtention(models.Model):
    _inherit = 'hr.employee'


    def employee_working_hours(self):
        employee_data = self.env['hr.employee'].search([])
        emp_master_data = {}
        emp_name = []
        emp_join_date = []
        emp_resign_date = []
        emp_working_hours = []
        for emp in employee_data:
            emp_name.append(emp.name)
            emp_join_date.append(emp.create_date)
            if emp.departure_date:
                emp_resign_date.append(emp.departure_date)
            else:
                emp_resign_date.append(datetime.today().date())
            emp_working_hours.append(emp.resource_calendar_id.hours_per_day)

        emp_master_data['name'] = emp_name
        emp_master_data['join_date'] = emp_join_date
        emp_master_data['resign_date'] = emp_resign_date
        emp_master_data['working_hours'] = emp_working_hours

        return emp_master_data





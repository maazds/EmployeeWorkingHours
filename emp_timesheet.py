import streamlit as st
import odoorpc
import pandas as pd


odoo = odoorpc.ODOO('localhost', port=8069)


odoo.login('odoodevelopmentdb', 'admin', 'admin')

# print(odoo.db.list())

if 'hr.employee' in odoo.env:
    employee_data = odoo.env['hr.employee'].employee_working_hours([[]])
    emp_df = pd.DataFrame.from_dict(employee_data)
    # print(emp_df)
    emp_df['join_date'] = pd.to_datetime(emp_df['join_date'])

    emp_df['resign_date'] = pd.to_datetime(emp_df['resign_date'])


    days = pd.Timedelta(days=1)

    emp_df['working_days'] = pd.NA

    for index, row in emp_df.iterrows():
        # print(index)
        # print(type(row))
        weekdays = []
        # working_dates = []
        join_date = row['join_date']
        resign_date = row['resign_date']
        while join_date <= resign_date:
            weekday = join_date.isoweekday()
            if weekday != 5 and weekday != 6:
                weekdays.append(join_date)
                # working_dates.append((join_date))
            join_date += days
        # emp_df['working_days_dates'] = working_dates
        emp_df.at[index, 'working_days'] = len(weekdays)
    emp_df['std_hours'] = emp_df['working_days'] * emp_df['working_hours']
    emp_df.to_csv('emp_df_final.csv')
    print(emp_df)






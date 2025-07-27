workers_name = input("Enter your name here:")
basic_salary = float(input("Enter your basic salary amount here:"))
monthly_allowance = float(input("Enter your monthly allowance:"))
gender = input("Enter your gender here:")
if gender == "male":
    tax = 25 / 100 * basic_salary
elif gender == "female":
    tax = 13 / 100 * basic_salary
else:
    print("INVALID BIODATA")

gross_pay = basic_salary + monthly_allowance
net_pay = gross_pay - tax
print(f'''
      Workers payment details
      Name:{workers_name.upper()}
      Salary:{basic_salary:,.2f}
      Allowance:{monthly_allowance:,.2f}
      Gender: {gender.upper()}
      Gross_pay:{gross_pay:,.2f}
      Net_pay:{net_pay:,.2f}
      ''')

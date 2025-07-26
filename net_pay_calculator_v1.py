print("== Net Pay calculator ==")

basic_salary = float(input("Enter your basic salary:"))
allowance = float(input("Enter your allowance here:"))
deduction = float(input("Enter total deduction e.g(pension tax)"))

gross_pay = basic_salary + allowance
net_pay = gross_pay - deduction
print(f"__\n salary details")
print(f"basic_salary is: {basic_salary:,.2f}")
print(f"Allowance is:{allowance:,.2f}")
print(f"Deduction is:{deduction:,.2f}")
print(f"Gross pay is: {gross_pay:,.2f}")
print(f"Net pay is: {net_pay:,.2f}")


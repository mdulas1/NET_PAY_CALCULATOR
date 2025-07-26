# A SIMPE NET_PAY_CALCULATOR
print("== Net pay calculator version 2 ==")
basic_salary = float(input("Enter your salary here\n>>"))
allowance = float(input("Enter your allowance here\n>>"))
gender = input("Select your gender type here\n>>")
if gender == "male":
    tax = 25 / 100 * basic_salary

elif gender == "female":
    tax = 13 / 100 * basic_salary
else:
    print("PLEASE SELECT YOUR GENDER TO PROCESSED")
gross_pay = basic_salary + allowance
net_pay = gross_pay - tax

print(f"YOUR BASIC_SALARY is :{basic_salary:,.2f} AND YOUR ALLOWANCE IS: {allowance:,.2f} YOUR NET_PAY IS: {net_pay:,.2f} AND YOUR GROSS_PAY IS:{gross_pay:,.2f}")




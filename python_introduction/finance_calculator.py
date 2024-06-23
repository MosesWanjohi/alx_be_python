monthly_income = input("Enter your monthly income: ")
total_monthly_expenses = input( "Enter your total  monthly expenses: ")
difference = float(monthly_income) - float(total_monthly_expenses)
print("Your monthly savings are", difference)
#Assume a simple annual interest rate of 5%.
#Calculate the projected savings after one year, incorporating the interest.
#Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
monthly_savings = difference
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest
print("Projected annual savings after one year, with interest, is: ", projected_savings)

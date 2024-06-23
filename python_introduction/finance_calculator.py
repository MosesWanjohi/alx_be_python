monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input( "Enter your total  monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are", monthly_savings)
#Assume a simple annual interest rate of 5%.
#Calculate the projected savings after one year, incorporating the interest.
#Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest
print("Projected annual savings after one year, with interest, is: ", projected_savings)

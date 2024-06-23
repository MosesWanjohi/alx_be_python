monthly_income = input("Enter your monthly income: ")
total_monthly_expenses = input( "Enter your total  monthly expenses: ")
difference = float(monthly_income) - float(total_monthly_expenses)
print("Your monthly savings are", difference)
#Assume a simple annual interest rate of 5%.
#Calculate the projected savings after one year, incorporating the interest.
#Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))

Monthly_Savings = difference
Annual_Savings = Monthly_Savings * 12
Interest = Annual_Savings * 0.05
Projected_Savings = Annual_Savings + Interest

print("Projected annual savings after one year, with interest, is: ", Projected_Savings)

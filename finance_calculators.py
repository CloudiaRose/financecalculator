'''this program allows the user to calculate the amount of interest they would earn on an investment
or the amount they would have to pay on a home loan.
the user inputs "investement" or "bond" to determine which calculation they'd like to do.
The input would not be case sensitive.
An error message will display if input is not valid.

simple interest formula:
A=P*math.pow((1+r),t)
where A=simple_investment_calculation
P=deposit
t=investment_years
r=investment_interest/100

compound interest formula
A=P*math.pow((1+r),t)
where A=compound_investment_calculation
P=deposit
t=investment_years
r=investment_interest/100  

bond repayment formula:
repayment=(i*P)/((1-(1+i)**(-n)) 
where i=converted_interest
P=house_value
n=repayment_months
'''
investment_choice=True
print("Welcome to the financial calculator!")

calculator_choice=input("Would you like to calculate interest on an investment, or bond repayment? Type 'investment' or 'bond' below. \n").lower()
import math
if calculator_choice =="investment":
  investment_choice=True
elif calculator_choice=="bond":
  investment_choice=False
else:
  print("You have not entered a valid option. Please try again.")
  calculator_choice=input("Would you like to calculate interest on an investment, or bond repayment? Type 'investment' or 'bond' below. \n").lower()

#algorithm for investment choice
if calculator_choice=="investment":
  deposit=float(input("How much would you like to deposit?"))
  investment_interest=float(input("How much is the interest rate on this deposit?"))
  investment_years=int(input("How many years would you like to invest?"))
  interest=input("Would you like simple or compound interest?")
#algorithm for simple interest
  if interest=="simple":
    simple_investment_calculation=float(deposit*(1+((investment_interest/100)*investment_years)))
    rounded_simple=round(simple_investment_calculation,2)
    print(f"Your total investment with simple interest is R{rounded_simple}") 
#algorithm for compound interest
  elif interest=="compound":
    compound_investment_calculation=float(deposit*math.pow(1+(investment_interest/100),investment_years)) 
    rounded_compound=round(compound_investment_calculation,2)
    print(f"Your total investment with compound interest is R{rounded_compound}")
  else:
    print("You have not entered a valid choice. Please try again.") 

#algorithm for bond repayment choice
if calculator_choice=="bond":
  house_value=int(input("Please enter the value of the house: R"))
  bond_interest=float(input("Please enter the percent interest rate on the bond: "))
  repayment_months=int(input("Please enter the number of months for repayment: "))
  converted_interest=(bond_interest/100)/12
  bond_repayment=float(converted_interest*house_value)/(1-(1+converted_interest)**(-repayment_months))
  rounded_repayment=round(bond_repayment,2)
  print(f"Your bond repayment will be R{rounded_repayment} per month, over {repayment_months} months.")


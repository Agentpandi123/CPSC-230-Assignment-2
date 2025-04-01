'''Add if statements to check that the sale price and sales tax are valid values, that is, not negative. If they are, prompt the user 
of their mistake. Your program should only continue to ask for sales tax rate if the sale price is positive. '''

import math
Cost = float(input("What was the total price of your items: ")) #Ask user what the costs of the items were
Tax = float(input("What is the salex tax rate in your area: ")) #Ask user what sales tax rate is

while Cost < 0:
    print("You made a mistake. Enter a positive number cost.")
    Cost = float(input("What was the total price of your items: ")) #Re-ask the user for a new cost because his original is negative

#find the total tax amount
TotalTax = Cost * (Tax / 100)
#add the tax and original cost
TotalCost = TotalTax + Cost
#Print total cost
print("The total cost of all your itmes including sales tax is ", TotalCost)
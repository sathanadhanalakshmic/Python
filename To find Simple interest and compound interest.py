p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter number of years:"))
si=(p*r*t)/100
ci=p*(1+(r/100))**t-p
print("Simple interest=",si)
print("Compound interest=",ci)

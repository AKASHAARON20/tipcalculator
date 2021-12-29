#If the bill was $150.00, split between 5 people, with 12% tip. 


print("Welcome to the tip calculator!")
bill =float(input("What was the total bill?" ))
tip = int(input("How much tip would you like to give?10,12,or 15?"))
ppl = int(input("How many people to split the bill?"))
tippercentage=(tip/100)
totalbillp =bill*tippercentage
totalfbill = totalbillp + bill
totalbill =  totalfbill / ppl
pp= round(totalbill,2)
print("Each person should pay:",pp)



#This will predict sales
#02/19/2019
#CTI-110 P2T1 - Sales prediction
#Nathan Ake

#varibles

sales=0.0

#input sales amount
sales= float(input("Enter the total sales amount: "))

#caulate
profit=sales * .23

#display the predicted amount
print("Estimated profit will be $", format(profit,'.2f'),".",sep="")


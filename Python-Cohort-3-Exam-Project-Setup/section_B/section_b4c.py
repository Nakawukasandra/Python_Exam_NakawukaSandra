#Values X1 = 60, X2 =30, Y1 = 160.5, Y2 = 97.7
#(formula d = math.sqrt (X1-X2) (Y1-Y2))

import math

X1 = 60
X2 = 30 
Y1 =160.5
Y2 = 97.7

X1 = int(input('Enter the value of X1:\t'))
X2 = int(input('Enter the value of X2:\t'))
Y1 = float(input('Enter the value of Y1:\t'))
Y2 = float(input('Enter the value of Y2:\t'))

simplifiedExpression = (X1-X2) ** 2 + (Y1-Y2) ** 2
d = math.sqrt(simplifiedExpression)

print(d)
print("The value of d is:\t" +  str(d)) 
print("The value of d is: %.2f " %d )
print(f"The value of d is: {d}")

    

'''Add an if statement to check if the value of the discriminate is negative. If the discriminate is negative prompt the user. 
Also, your program should not continue with the square root calculation, hence avoiding the "math domain error".'''

from cmath import sqrt
import math

#Ask for values of A, B, C
A = float(input("What is the value of A: "))
B = float(input("What is the value of B: "))
C = float(input("What is the value of C: "))


D = (B ** 2) - (4 * A * C ) # Make the square root easier to understand 

while D < 0:
    print("The discriminate is negative, choose another number. ") # Tell the user if the discriminate is negatice
    A = float(input("What is the value of A: ")) # Ask questions again
    B = float(input("What is the value of B: "))
    C = float(input("What is the value of C: "))
    D = (B ** 2) - (4 * A * C ) # Redo the value of 
else: 
    Output1 = (-B + sqrt(D)) / (2 * A) # Find 2 different outputs
    Output2 = (-B - sqrt(D)) / (2 * A)
    print("The outputs are x = ", Output1, " and x = ", Output2) # print different outputs
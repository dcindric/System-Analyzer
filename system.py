#Project name: System analyzer, v.1.0: Based on the given transfer function of linear time invariant system,
#various representations of the systems behavior are shown (pole - zero plot, Bode diagram, Nyquist diagram,...)
#Author: Dino Cindric
#Licence: Creative Common Licence - Free for use and modifying

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


def tf_poles (transfer_function):
    poles = transfer_function.poles
    print("\nPoles of given transfer function: ")
    
    for i in poles:
        print(i)

    return poles

def tf_zeros (transfer_function):
    zeros = transfer_function.zeros
    print("\nZeros of give transfer function: ")

    for i in zeros:
        print(i)

    return zeros


while(True):

    numOrder = int(input("Enter numerator order: "))
    denOrder = int(input("Enter denominator order: "))

    if (numOrder > denOrder):
        print("Order of numerator must be lower or equal to the order of denominator!")
    else:
        break


numCoeff = [None] * (numOrder + 1)
denCoeff = [None] * (denOrder + 1)


#Input of numerator coeff.
for i in range(len(numCoeff)):
    print("Enter ", len(numCoeff) - i - 1, ". numerator coefficent:")
    numCoeff[i] = int(input(" "))


#Input of denominator coeff.
for i in range(len(denCoeff)):
    print("Enter ", len(denCoeff) - i - 1, ". denominator coefficent:")
    denCoeff[i] = int(input(" "))
    

#Creating transfer function from numerator and denominator
tf = signal.TransferFunction(numCoeff, denCoeff)    

poles = tf_poles(tf)            
zeros = tf_zeros(tf)


poloviReal = [None] * len(poles)





figure1 = plt.figure()


plt.title("Pole - zero plot")
plt.xlabel("Real axis")
plt.ylabel("Imaginary axis")
plt.title("Pole - zero plot")
plt.grid()


plt.plot(poles.real, poles.imag, 'rx', label = "Poles")
plt.plot(zeros.real, zeros.imag, 'bo', label = "Zeros")

plt.legend()
plt.show()
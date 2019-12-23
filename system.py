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

def pole_zero_plot (poles, zeros):

    plt.title("Pole - zero plot")
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    plt.grid()


    plt.plot(poles.real, poles.imag, 'rx', label = "Poles")
    plt.plot(zeros.real, zeros.imag, 'bo', label = "Zeros")
    plt.legend()
    plt.savefig("Pole - zero plot")



def bode_diagram (transfer_function):

    #Calculating Bode magnitude and phase data from given transfer function of LTI
    w, mag, phase = signal.bode(transfer_function)

    #Figure with 2 rows and 1 column - first for amplitude, second for phase data
    plt.subplot(2,1,1)
    plt.title("Bode diagram")

    #Plotting amplitude vs frequency graph
    plt.semilogx(w, mag)
    plt.grid()
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Amplitude (dB)")


    #Plotting phase vs frequency graph
    plt.subplot(2,1,2)
    plt.semilogx(w, phase)
    plt.grid()
    plt.xlabel("Frequency (rad/s)")
    plt.ylabel("Phase (deg)")

    #Saving figure in png format
    plt.savefig("Bode diagram.png")




while(True):

    num_order = int(input("Enter numerator order: "))
    den_order = int(input("Enter denominator order: "))

    if (num_order > den_order):
        print("Order of numerator must be lower or equal to the order of denominator!")
    else:
        break


num_coeff = [None] * (num_order + 1)
den_coeff = [None] * (den_order + 1)


#Input of numerator coeff.
for i in range(len(num_coeff)):
    print("Enter ", len(num_coeff) - i - 1, ". numerator coefficent:")
    num_coeff[i] = int(input(" "))


#Input of denominator coeff.
for i in range(len(den_coeff)):
    print("Enter ", len(den_coeff) - i - 1, ". denominator coefficent:")
    den_coeff[i] = int(input(" "))
    

#Creating transfer function from numerator and denominator
tf = signal.TransferFunction(num_coeff, den_coeff)    

poles = tf_poles(tf)            
zeros = tf_zeros(tf)


pole_zero_plot(poles, zeros)
bode_diagram(tf)


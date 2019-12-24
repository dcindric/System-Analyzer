#Project name: System analyzer, v.1.0: Based on the given transfer function of linear time invariant system,
#various representations of the systems behavior are shown (pole - zero plot, Bode diagram, Nyquist diagram,...)
#Author: Dino Cindric
#Licence: Creative Common Licence - Free for use and modifying

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os
import sys


def save_fig ():

    save_check = input("Do you want to save current figure (Y/n) ? ")


    while(True):

        if (save_check == "Y" or save_check == "y"):
            file_name = input("Enter file name: ")
            plt.savefig(file_name)
            print("File saved successfully!")
            break

        elif (save_check == "n" or save_check == "N"):
            break

        else:
            print("Wrong input, enter 'Y' for saving or 'n' for not saving current figure!")
        


#Calculating poles of the transfer function
def tf_poles (transfer_function):

    poles = transfer_function.poles
    print("\nPoles of given transfer function: ")
    
    for i in poles:
        print(i)

    return poles


#Calculating zeros of the transfer function
def tf_zeros (transfer_function):

    zeros = transfer_function.zeros
    print("\nZeros of give transfer function: ")

    for i in zeros:
        print(i)

    return zeros


#Creating pole-zero plot 
def pole_zero_plot (poles, zeros):

    plt.figure()

    plt.title("Pole - zero plot")
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    plt.grid()


    plt.plot(poles.real, poles.imag, 'rx', label = "Poles")
    plt.plot(zeros.real, zeros.imag, 'bo', label = "Zeros")
    plt.legend()
    
    plt.tight_layout()
    save_fig()

#Displaying Bode diagram
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

    save_fig()



#Displaying Nyquist diagram
def nyquist_diagram (transfer_function):
    w, H = signal.freqresp(transfer_function)

    plt.figure()
    plt.title("Nyquist diagram")
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    plt.grid()
    
    plt.plot(H.real, H.imag, "b")
    plt.plot(H.real, -H.imag, "b")

    plt.tight_layout()
    # plt.savefig("Nyquist diagram")
    save_fig()

#Calculating and displaying impulse response of the system
def impulse_response (transfer_function):

    #Impulse method returns two n-dimensional arrays: t (time) and y (response values)
    #Dimensions of each array can be specified with additional arguments
    t, y = signal.impulse(transfer_function)
    
    plt.figure()
    plt.title("Impulse response of the system")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.grid()

    #Plot y vs t 
    plt.plot(t, y)
    plt.tight_layout()

    save_fig()

#Calculating and displaying step response of the system
def step_response (transfer_function):

    #Step method returns two n-dimensional arrays: t (time) and y (response values)
    #Dimensions of each array can be specified with additional arguments
    t, y = signal.step(transfer_function)

    plt.figure()
    plt.title("Step response of the system")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.grid()

    #Plot y vs t
    plt.plot(t, y)
    plt.tight_layout()

    save_fig()


#Input of data necessary to create transfer function of the system
def data_input ():

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
            num_coeff[i] = float(input(" "))


        #Input of denominator coeff.
        for i in range(len(den_coeff)):
            print("Enter ", len(den_coeff) - i - 1, ". denominator coefficent:")
            den_coeff[i] = float(input(" "))
    
        return num_coeff, den_coeff




num_coeff, den_coeff = data_input()
 

#Creating transfer function from numerator and denominator
tf = signal.TransferFunction(num_coeff, den_coeff)    

poles = tf_poles(tf)            
zeros = tf_zeros(tf)


pole_zero_plot(poles, zeros)
bode_diagram(tf)
nyquist_diagram(tf)
impulse_response(tf)
step_response(tf)
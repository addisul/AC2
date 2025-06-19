import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from scipy.signal import argrelextrema
from scipy.fft import fft, ifft, fftfreq
pi = np.pi

def choose_directory():
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        directory_path = filedialog.askdirectory()
        return directory_path
    
def choose_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename()
    return file_path

directory = choose_directory()
if directory:
        os.chdir(directory)
        print(f"Current directory: {os.getcwd()}")
else:
        print("No directory selected.")

file = choose_file()

print(f"file is: {file}")

data = np.loadtxt(file)
data_num = np.array(data)
s = np.shape(data)
print(s)

steps = data_num[:,0]
AB = data_num[:,5] # |aH>
AC = data_num[:,6] # |aV>
AD = data_num[:,7] # |b>

font = {'size': 16}
plt.rc('font', **font)

plt.figure(1)  # Create a new figure for each plot
plt.plot(steps, AB, '.', color = 'b')
plt.plot(steps, AC, '.', color = 'r')
plt.plot(steps, AD, '.', color = 'g')

plt.xlabel('steps')
plt.ylabel('coincidence counts')
plt.legend(['H','V','b'])
plt.show()

#normalize everything relative to itself

ABnorm = (AB - min(AB))/max(AB-min(AB))
ACnorm = (AC - min(AC))/max(AC-min(AC))
ADnorm = (AD - min(AD))/max(AD-min(AD))

plt.figure(figsize=(6,5.5))
plt.plot(steps, ABnorm, '.', color = 'b')
plt.plot(steps, ACnorm, '.', color = 'r')
#plt.plot(steps, ADnorm, '.', color = 'g')

plt.xlim(50,110)
plt.ylim(.4,1)

plt.xlabel('steps')
plt.ylabel('coincidence counts')
plt.legend(['|aH>','|aV>','|b>'])
plt.savefig('grover_test_2.pdf')

plt.show()

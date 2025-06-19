import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from scipy.signal import argrelextrema
from scipy.fft import fft, ifft, fftfreq

"""
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
"""
df = pd.read_csv(('.txt'))

data = pd.read_excel("LaserPlotwithwaveplate.xls") #read file code
angle = pd.read_excel("LaserPlotwithwaveplate.xls")['Angle(degrees)'].tolist()
power = pd.read_excel("LaserPlotwithwaveplate.xls")['Power(mW)'].tolist()

plt.scatter(angle,power, color = 'blue') #plot x versus y (angle vs power) 

#plt.title('Power vs Angle of Polarizer') #chart title

plt.show
plt.savefig("plot.pdf")
print(angle,power)

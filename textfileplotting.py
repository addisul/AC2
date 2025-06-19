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

plt.rcParams['font.size'] = 16

steps = data[:,0]
H_conic = data[:,5]

plt.plot(steps, H_conic, ".")
plt.xlabel('steps', fontsize = 20)
plt.ylabel('counts', fontsize = 20)
plt.show()

plt.savefig("plot1.pdf")

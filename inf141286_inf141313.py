import scipy
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import wavfile
import wave, struct
import cmath
import sys
import os.path
from os import path

def main():
    if ((len(sys.argv) < 2) or (len(sys.argv) > 2)):
        print("Wrong number of arguments")
        return
    filename = sys.argv[1]
    if (path.exists(filename) == False):
        print("Wrong file path")
        return
    
    y1, signal1 = scipy.io.wavfile.read(filename)
    window = signal.tukey(len(signal1))
    signalWindow = window * signal1
    signalFFT = np.fft.fft(signalWindow)
    signalFFTabs = np.log(np.abs(signalFFT))
    maxValue1 = max(signalFFTabs)
    maxValue2 = maxValue1
    product = [0 for i in range(int(len(signal1)/8))]
    for i in range(int(len(signal1)/8)):
        product[i] = signalFFTabs[i] * signalFFTabs[2*i] * signalFFTabs[3*i] * signalFFTabs[4*i]
        if ((product[i] > maxValue2) and (i >= (65 * len(signal1)/y1)) and (i <= (275 * len(signal1)/y1))):
            maxValue2 = product[i]
            fundFreq = i
    fundFreq1 = fundFreq * y1 / len(signal1)
    
    if (fundFreq1 >= 165):
        answer = 'K'
    else:
        answer = 'M'
    
    print(answer)

if __name__ == "__main__":
    main()
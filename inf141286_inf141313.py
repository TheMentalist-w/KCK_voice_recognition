from scipy import signal
from numpy import fft, log, zeros
#import numpy as np
#import pandas as pd
from scipy.io import wavfile
#import wave
#import struct
from sys import argv
from os import path

def process(signal1):
    window = signal.tukey(len(signal1))
    signalWindow = window * signal1
    signalFFT = fft.fft(signalWindow)
    signalFFTabs = log(abs(signalFFT))
    return signalFFTabs

def main():
    if len(argv) != 2:
        print("Wrong number of arguments")
        return
    filename = argv[1]

    try:
        y1, signal1 = wavfile.read(filename)
    except OSError:
        print("Wrong file path")
        return
    signalFFTabs = process(signal1)
    maxValue2 = 0
    product = zeros(int(len(signal1)/8), dtype=float)
    for i in range(int(len(signal1)/8)):
        product[i] = signalFFTabs[i] * signalFFTabs[2*i] * signalFFTabs[3*i] * signalFFTabs[4*i]
        if ((product[i] > maxValue2) and (i >= (65 * len(signal1)/y1)) and (i <= (275 * len(signal1)/y1))):
            maxValue2 = product[i]
            fundFreq = i
    fundFreq1 = fundFreq * y1 / len(signal1)
    answer = 'K' if fundFreq1 >= 165 else 'M'
    print(answer)


if __name__ == "__main__":
    main()

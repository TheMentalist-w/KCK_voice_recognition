import scipy
from scipy import signal
import numpy as np
import pandas as pd
from scipy.io import wavfile
import wave
import struct
import sys
from os import path


def main():
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        return
    filename = sys.argv[1]

    try:
        y1, signal1 = scipy.io.wavfile.read(filename)
    except OSError:
        print("Wrong file path")
        return

    window = signal.tukey(len(signal1))
    signalWindow = window * signal1
    signalFFT = np.fft.fft(signalWindow)
    signalFFTabs = np.log(np.abs(signalFFT))
    maxValue2 = maxValue1 = max(signalFFTabs)
    product = [0 for i in range(int(len(signal1)/8))]
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

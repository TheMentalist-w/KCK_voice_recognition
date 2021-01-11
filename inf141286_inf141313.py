from scipy import signal
from numpy import fft, log, zeros
from scipy.io import wavfile
from sys import argv

def process(signal1):
    window = signal.tukey(len(signal1))
    signalWindow = window * signal1
    signalFFT = fft.fft(signalWindow)
    signalFFTabs = log(abs(signalFFT))
    return signalFFTabs

def main():
    filename = argv[1]
    y1, signal1 = wavfile.read(filename)

    signalFFTabs = process(signal1)
    maxValue2 = 0
    prod_count = int(len(signal1)/8)

    product = 0.0
    for i in range(prod_count):
        product = signalFFTabs[i] * signalFFTabs[2*i] * signalFFTabs[3*i] * signalFFTabs[4*i]
        if ((product > maxValue2) and (i >= (65 * len(signal1)/y1)) and (i <= (275 * len(signal1)/y1))):
            maxValue2 = product
            fundFreq = i
    fundFreq1 = fundFreq * y1 / len(signal1)
    answer = 'K' if fundFreq1 >= 175 else 'M'
    print(answer)
    # print(fundFreq1)


if __name__ == "__main__":
    main()

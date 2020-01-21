import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import gauss

s = pd.read_csv('NSR_datasets.csv')
s = s.values.tolist()


def only_val(x):
    for i in range(len(x)):
        s[i] = s[i][2]

    return s


def gaussian_noise(x_data):
    print("gaussian noise")
    sigma, mu = np.sqrt(np.var(x_data)), np.mean(x_data)
    list_1 = [0 for every in range(len(x_data))]
    noise = [gauss(mu, sigma) for something in list_1]
    gs_sig = np.array(noise) + np.array(x_data)

    return gs_sig

def poisson_noise(y_data):
    print("poisson noise")
    # lmbda =

clean_sig = only_val(s)
gaussian_sig = gaussian_noise(clean_sig)
plt.plot(gaussian_sig)
plt.show()

# df = np.array(only_val(s))
# # df = np.sin(40 * 2 * np.pi * t) + 0.5 * np.sin(90 * 2 * np.pi * t)
# t = np.array([v for v in range(0, (len(df)+1))])
# print(df[0:20])
#
# fft = np.fft.fft(df)
# T = t[1] - t[0]
# N = len(df)
#
# f = np.arange(0, 1/T, N)

# plt.ylabel("Amplitude")
# plt.xlabel("Frequency [Hz]")
# plt.bar(f[:N // 2], np.abs(fft)[:N // 2] * 1 / N, width=1)
# plt.show()

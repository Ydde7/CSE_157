# Imports
import matplotlib.pyplot as plt
import numpy as np
import csv as csv
import scipy as sci
import time

# This file uses np.fft.fft to provide frequency information.

def readCSV(filename):
     data_after = []
     with open(filename, 'r', newline ='') as csvdata:
            csvreader = csv.reader(csvdata, delimiter=',')
            for row in csvreader:
                    if (row[0] != ''):
                        data_after.append(float(row[0]))
            return data_after

def avg_filter(arr, N=3):
    """
    Filter to take an N-windowed average
        - arr = int or float array
        - N = window size
    """
    k_avg = np.repeat(1/N, N)
    return np.asarray(np.convolve(arr, k_avg, mode="valid"))

#=====================================================================

# Plot all data

grav = []

road = []


fig, axes = plt.subplots(2, figsize=(12,8), tight_layout=True)   # Create 2 blank graph figure

l1 = []
l2 = []
for i in range(1, 11):
    data1 = readCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Project/Code/Testing/CSE_157/data/dataset/Training/Gravel/gravel' + str(i) + '.csv')
    # Normalize about the mean
    data1 = data1 - np.mean(data1)
    freq = np.fft.fft(data1, n=100) # 100-point FFT provides frequency information up to 100hz
    axes[0].plot(freq[0:int(len(freq)/2)])
    l1.append("File " + str(i))
    grav.append(freq)

axes[0].set_title("Gravel Data")
axes[0].set_xlabel("Frequency (hz)")
axes[0].legend(l1)

for i in range(1, 11):
    data2 = readCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Project/Code/Testing/CSE_157/data/dataset/Training/Road/road' + str(i) + '.csv')
    # Normalize about the mean
    data2 = data2 - np.mean(data2)
    freq = np.fft.fft(data2, n=100) # 100-point FFT provides frequency information up to 100hz
    axes[1].plot(freq[0:int(len(freq)/2)])
    l2.append("File " + str(i))
    road.append(freq)

axes[1].set_title("Road Data")
axes[1].set_xlabel("Frequency (hz)")
axes[1].legend(l2)

plt.show()

# Print the sum of all the data as a single graph

grav_sum = grav[0]
road_sum = road[0]

fig2, axes2 = plt.subplots(2, figsize=(12,8), tight_layout=True)   # Create 2 blank graph figure


for i in range(1, len(grav) -1):
     grav_sum = grav_sum + grav[i]
     road_sum = road_sum + road[i]

# grav_sum = grav_sum / len(grav)
# road_sum = road_sum / len(road_sum)

grav_sum = avg_filter(grav_sum, N=5)
road_sum = avg_filter(road_sum, N=5)


axes2[0].plot(grav_sum[0:int(len(grav_sum)/2)])
axes2[0].set_title("Fit Gravel FFT Data")
axes2[0].set_xlabel("Frequency (hz)")
axes2[0].set_ylabel("Amplitude")

axes2[1].plot(road_sum[0:int(len(road_sum)/2)])
axes2[1].set_title("Fit Road FFT Data")
axes2[1].set_xlabel("Frequency (hz)")
axes2[1].set_ylabel("Amplitude")

plt.show()


# # Main
# data = readCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Project/Code/Testing/CSE_157/data/dataset/Training/Gravel/gravel1.csv')
# data2 = readCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Project/Code/Testing/CSE_157/data/dataset/Training/Road/road6.csv')
# data3g = readCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Project/Code/Testing/CSE_157/data/dataset/Training/Gravel/gravel2.csv')
# data4r = readCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Project/Code/Testing/CSE_157/data/dataset/Training/Road/road5.csv')
# fig, axes = plt.subplots(2, figsize=(12,8))   # Create 2 blank graph figure

# # Centers the data

# data = data - np.mean(data)
# data2 = data2 - np.mean(data2)
# data3g = data3g - np.mean(data3g)
# data4r = data4r - np.mean(data4r)

# axes[0].plot(data)
# freq = np.fft.fft(data, n=100) # 100-point FFT provides frequency information up to 100hz
# axes[1].plot(freq)
# plt.show()

# fig2, axes2 = plt.subplots(2, figsize=(12,8))   # Create 2 blank graph figure

# axes2[0].plot(data2)
# freq2 = np.fft.fft(data2, n=100) # 100-point FFT provides frequency information up to 100hz
# axes2[1].plot(freq2)
# plt.show()

# freq3 = np.fft.fft(data3g, n=100)

# plt.plot(freq[0:int(len(freq)/2)])
# plt.plot(freq2[0:int(len(freq2)/2)])
# plt.plot(freq3[0:int(len(freq3)/2)])
# plt.legend(['freq_gravel1','freq_road6', 'freq_gravel2'])
# plt.show()


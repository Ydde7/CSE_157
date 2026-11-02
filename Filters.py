# ===============================================================================

# This is a test program to apply different filters to our data (static implementation)

    # Refer to New Analyze.py in src, this si just to test filters and their effects

# ===============================================================================

import matplotlib.pyplot as plt
import numpy as np
import csv as csv

data_after = []
def readCSV(filename):
    data_after = [] 
    with open(filename, 'r') as csvdata:
        csvreader = csv.reader(csvdata)
        for row in csvreader:
            val = ''.join(row).lstrip("\"'\n ")
            if (val != ''):
                data_after.append(float(val))
    return data_after

d1 = readCSV('data/tent_imu.csv')
b1 = readCSV('data/tent_imu_2.csv')

# # LPF?
# d2 = []
# d2.append(d1[0])
# for i in range(1, len(d1)):
#     d2.append(d1[i] + d1[i-1])

# Moving average:
def avg(arr):
    # 5 item average with 0 paddings
    d3 = []
    d3.append(arr[0])
    for i in range(1, len(arr)-1):
        d3.append((arr[i-1]+arr[i]+arr[i+1])/3)
    d3.append(arr[-1])
    return d3

# alternatively
avg_kernel = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]

# c1 = np.correlate(d1, b1, 'full')


plt.plot(d1)
# plt.plot(d3)
# plt.legend()
# plt.show()

# plt.plot(d1)
# plt.show()
# # plt.plot(d2)
# # plt.plot(d3)
# plt.show()
# plt, axs = plt.subplots(1,2)
# axs[0].plot(d1)
# axs[0].set_title("Raw Signal")
# axs[1].plot(d2)
# axs[1].set_title("Simple LPF")

# Smoothing Kernel Tests =================================
# Test simple smooth kernel

sm_kernel = [1,-2,1] # LPF
sm_kernel2 = [-1, 2, -1] # HPF

    # First is the base
smoothed = np.convolve(d1, sm_kernel, mode='full') # LPF?

smoothed2 = np.convolve(d1, sm_kernel2, mode='full') # HPF?

plt.plot(avg(np.asarray(smoothed2)))
plt.plot(avg(np.asarray(smoothed)))

# Moving avg Tests =================================
# Averaged with kernel

avg_window = np.convolve(d1, avg_kernel, mode='full')

plt.plot(np.asarray(avg_window))

plt.legend(['sm_kern', 'sm_kern_2', 'avg_win'])
# plt.plot(c1)
plt.show()

# Filter Tests =================================
# trying a gradient filter: (1st derivative)
    # Sobel inspired
grad_kernel = [1, -2, 0, 2, 1]

grad = np.convolve(d1, grad_kernel)  # using normalized smoothed value
plt.plot(grad)
plt.show()

# Window Tests =================================
# Idea: Downsample with a kernel then apply a filter

k_dsmpl = [1,0,1,0] # Take half the values This is wrong, down sampling is defined as x[n] = x[nM]

print(d)

# plt.plot(d1)
# plt.plot(down_sampled)
# plt.show()











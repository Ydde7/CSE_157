import matplotlib.pyplot as plt
import numpy as np
import csv as csv
import serial
import scipy as sci

# ===========================================

# (!) Using data taken at a previous time with Lab 05 code (!)

# # Identify port type
# spt = serial.Serial('COM8', baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
# serialString = ""  # For UART data holding
# iteration = 0      # Limit data before truncating and restarting csv list (max data: 10000 points)
# cont = True        # Checks if data collection should continue
# has_data = False   # Set true after run once

# dest = "C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Labs/Lab_06/data/filtered.csv"

# total_samples = 10000

# # Save data to .csv file
# print("Starting ...")
# while(cont):
#     if (iteration > 0):
#         with open(dest, 'w', newline='') as dataFile:
#             dataFile.close()
#         iteration = 0

#     with open(dest, 'w', newline='') as dataFile:
#         while iteration < total_samples: 
#             serialString = spt.readline()
#             csvWrite = csv.writer(dataFile, delimiter=',')

#             try:
#                 val = [serialString.decode("Ascii")]
#                 csvWrite.writerow([serialString.decode("Ascii")])      
#                 print(str(serialString.decode("Ascii"))) 
#                 iteration += 1
#             except:
#                 pass

#             if(iteration % 100 == 0):
#                   print(f"Iteration: {iteration}")
            
#         dataFile.close()
    # cont = False
    # has_data = True

# ===========================================

def writeCSV(arr, dest = "C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Labs/Lab_06/data/filtered.csv"):
    with open(dest, 'w', newline='') as reset:
            reset.close()
    with open(dest, 'a', newline='') as dataFile:
            csvWrite = csv.writer(dataFile, delimiter=',')
            # csvWrite.writerow(arr)
            for i in range(0, len(arr)-1):
                 csvWrite.writerow([arr[i]])
            dataFile.close()
    print("Wrote to CSV")

def readSerialCSV(filename):
    data_after = [] 
    with open(filename, 'r') as csvdata:
        csvreader = csv.reader(csvdata)
        for row in csvreader:
            val = ''.join(row).lstrip("\"'\n ")
            if (val != ''):
                data_after.append(float(val))
    return data_after

def readCSV(filename):
     data_after = []
     with open(filename, 'r', newline ='') as csvdata:
            csvreader = csv.reader(csvdata, delimiter=',')
            for row in csvreader:
                    data_after.append(float(row[0]))
            return data_after
     

d1 = readSerialCSV('C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Labs/Lab_06/data/data.csv')

def avg_filter(arr, N=3):
    k_avg = np.repeat(1/N, N)
    return np.asarray(np.convolve(arr, k_avg, mode="valid"))


def ns(arr, sig=2, N=12):
    """
    Applys the 1d gaussian filter from scipy, then 
    Normalizes the signal around 0 using a [1, -2, 1] kernel.
    Finally applies a windowed average and returns the values normalized between -1 to 1.

    - All filters are applied with mode="valid"

    ======

    - arr = Input signal (np.array)

    - sig = Standard Deviation for the gaussian filter

    - N = average filter size

    """
    k_n = [1, -2, 1]    # High pass like?
    k_avg = np.repeat(1/N, N)

    # n = np.asarray(arr) / max(arr) # Normalize
    n = arr

    g_smooth = sci.ndimage.gaussian_filter1d(n, sig) # With std deviation of 2

    zeroed = np.asarray(np.convolve(g_smooth, k_n, mode="valid"))

    averaged = np.asarray(np.convolve(zeroed, k_avg, mode="valid")) 

    return averaged / max(averaged)
  

def energyTotal(arr):
     """
    Returns the energy of the input signal
        - Recall our filtered signal is normalized so these values are in relation to a normalized signal.
     """
     a = np.abs(arr)
     sq = a**2
     return np.cumsum(sq)[-1]

def thresh(arr, cutoff=0.5):
    """
    Returns a binary yes or no based on whether or not we are driving on gravel
    """
    a = np.array(arr)
    condlist = [a < cutoff, a >= cutoff]
    oplist = [0, 1]
    return np.select(condlist, oplist)


plt.plot(d1)
plt.title("Raw Signal")
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

filtered = np.asarray(ns(d1, sig=2, N=21))
writeCSV(filtered)

plt.plot(filtered)
plt.title("Normalized Signal")
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

print("Energy = " + str(energyTotal(filtered)) + " Joules")
dest = "C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Labs/Lab_06/data/energy.csv"
energy = np.abs(filtered)
writeCSV(energy, dest=dest)
plt.plot(energy)
plt.title("Energy of Signal")
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.show()

dest = "C:/Users/Ydde7/Desktop/Merced/Sem_F26/CSE 157/Labs/Lab_06/data/threshold.csv"
threshold = thresh(energy, cutoff=0.4)
writeCSV(threshold, dest=dest)
plt.plot(filtered)
plt.plot(threshold)
plt.ylim([0, 2])
plt.title("Threshold")
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend(["Filtered Signal", "Threshold"])
plt.show()





# Testing filters: ----------------------------
# g_smooth = sci.ndimage.gaussian_filter1d(d1, 2) # With std deviation of 2

# plt.plot(d1)
# plt.show()

# k_avg3 = [1/3, 1/3, 1/3]
# k_avg9 = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
# k_zero = [1, -2, 1]

# k_avg12 = np.repeat(1/12, 12)
# print(k_avg12)

# plt.plot(g_smooth)
# plt.plot(np.asarray(np.convolve(g_smooth, k_avg3, mode="valid")))
# plt.show()

# plt.plot(g_smooth)
# plt.plot(np.asarray(np.convolve(g_smooth, k_avg9, mode="valid")))
# plt.show()

# plt.plot(g_smooth)
# plt.plot(np.asarray(np.convolve(g_smooth, k_avg12, mode="valid")))
# plt.show()

# plt.plot(g_smooth)
# zeroed = np.asarray(np.convolve(g_smooth, k_zero, mode="valid"))
# plt.plot(np.asarray(np.convolve(zeroed, k_avg12, mode="valid")))
# plt.show()

# # Moving average:
# def avg(arr):
#     # 5 item average with 0 paddings
#     d3 = []
#     d3.append(arr[0])
#     for i in range(1, len(arr)-1):
#         d3.append((arr[i-1]+arr[i]+arr[i+1])/3)
#     d3.append(arr[-1])
#     return d3

# # alternatively
# avg_kernel = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]

# # c1 = np.correlate(d1, b1, 'full')


# plt.plot(d1)
# Testing filters: ----------------------------


# # Smoothing Kernel Tests =================================
# # Test simple smooth kernel

# sm_kernel = [1,-2,1] # LPF
# sm_kernel2 = [-1, 2, -1] # HPF

#     # First is the base
# smoothed = np.convolve(d1, sm_kernel, mode='full') # LPF?

# smoothed2 = np.convolve(d1, sm_kernel2, mode='full') # HPF?

# plt.plot(avg(np.asarray(smoothed2)))
# plt.plot(avg(np.asarray(smoothed)))

# # Moving avg Tests =================================
# # Averaged with kernel

# avg_window = np.convolve(d1, avg_kernel, mode='full')

# plt.plot(np.asarray(avg_window))

# plt.legend(['sm_kern', 'sm_kern_2', 'avg_win'])
# # plt.plot(c1)
# plt.show()

# # Filter Tests =================================
# # trying a gradient filter: (1st derivative)
#     # Sobel inspired
# grad_kernel = [1, -2, 0, 2, 1]

# grad = np.convolve(d1, grad_kernel)  # using normalized smoothed value
# plt.plot(grad)









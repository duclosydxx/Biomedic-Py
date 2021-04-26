import time
from bitalino import BITalino
import numpy as np
import matplotlib.pyplot as plt
from biosppy import storage
from biosppy.signals import ecg



# The macAddress variable on Windows can be "XX:XX:XX:XX:XX:XX" or "COMX"
# while on Mac OS can be "/dev/tty.BITalino-XX-XX-DevB" for devices ending with the last 4 digits of the MAC address or "/dev/tty.BITalino-DevB" for the remaining
macAddress = "/dev/tty.BITalino-40-33-DevB"
# This example will collect data for 5 sec.
running_time = 5

batteryThreshold = 30
acqChannels = [0, 1, 3]
samplingRate = 1000
nSamples = 100
digitalOutput = [1, 1]


# Connect to BITalino
device = BITalino(macAddress)

# Set battery threshold
device.battery(batteryThreshold)

# Read BITalino version
print(device.version())

# Start Acquisition
device.start(samplingRate, acqChannels)

start = time.time()
end = time.time()
myTab = []
tabX = [0]*30000
tabY = [0]*30000
myTab = device.read(30000)



# Turn BITalino led on
device.trigger(digitalOutput)




# Stop acquisition
device.stop()

# Close connection
device.close()

for i in range(0, 30000):
    tabX[i] = i
    tabY[i] = myTab[i][6]

mynpArr = np.array(tabY)
np.savetxt("array.txt", mynpArr, fmt="%s")

# load raw ECG signal
signal, mdata = storage.load_txt('array.txt')

# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)
tabFC = []
ecg._extract_heartbeats(signal=signal, before=tabFC)
print tabFC


plt.plot(tabX, tabY)
plt.show(block=True)



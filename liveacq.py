import time
from bitalino import BITalino
import numpy as np
import matplotlib.pyplot as plt

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

i = 0
i1 = 0
i2 = 1
x = [0]*1000
y2 = [0]*1000
fact = 0

tps = time.time()

plt.show()

while 1:
    if time.time() - tps >= 0.35 :

        for i in range(0, 1000):
            x[i] = (fact*1000)+(i+1)
        print x
        fact = fact+1

        y = device.read(1000)
        for i in range(0, 1000):
            y2[i] = y[i][6]
        print y2

        i1 = i2
        i2 = i2+1
        plt.plot(x, y2)
        plt.pause(0.05)


        tps = time.time()

# Turn BITalino led on
device.trigger(digitalOutput)




# Stop acquisition
device.stop()

# Close connection
device.close()

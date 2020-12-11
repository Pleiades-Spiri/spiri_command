from pymavlink import mavutil
from drone import Drone,Location
# Create the connection
# From topside computer
import time



targetAltitude = 2

DD = Drone('127.0.0.1:14581')
DD.arm_and_takeoff(2,auto_mode=False)
while True:
     print("Altitude:",DD.location.altR)
     if DD.location.altR > 0.95 * targetAltitude:
         print("break")
         break



time.sleep(3)
print("Execute LAND")
DD.set_flight_mode('MISSION')

time.sleep(3)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
##======================================================================
##        Copyright (C) 2020 Tong He
##        All rights reserved
##        Machine Name:           Tong
##        File Name:              spiri
##        Build Year:             2020
##        created by Tong He at   06/12/2020
##======================================================================


# Import mavutil
from pymavlink import mavutil
import time
from spiri import Drone, Location
import time

drone = Drone('127.0.0.1:14550')
targetAltitude = 2.5
drone.arm_and_takeoff(targetAltitude)
while True:
    print("Altitude:", drone.location.altR)
    if drone.location.altR > 0.95 * targetAltitude:
        print("break")
        break
time.sleep(2)
drone.set_flight_mode('LAND')
time.sleep(1)

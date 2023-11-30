import time
from pymavlink import mavutil
from general.conn import master

def d_arm():
    # changing to guided mode
    master.set_mode(4)

    # Arm the vehicle
    master.arducopter_arm()
    time.sleep(5)

    print("The vehicle is ARMED...")

d_arm()
import time
from pymavlink import mavutil
from general.conn import master

def d_m_auto():
    # changing to guided mode
    master.set_mode(3)

    print("Mode changed to AUTO")
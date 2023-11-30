import time
from pymavlink import mavutil
from general.conn import master

def d_mov_glo():
    master.wait_heartbeat()

    print("Target Sustem : ",master.target_system, "Target_Component : ", master.target_component)

    lat = float(input("Enter the Latitude : "))
    lon = float(input("Enter the Longitude : "))
    alt = float(input("Enter the Altitude : "))

    # Fly to a waypoint (replace coordinates with your desired waypoint)

    master.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, master.target_system,
                            master.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, int(0b110111111000),
                            int(lat * 10 ** 7), int(lon * 10 ** 7), alt, 0, 0, 0, 0, 0, 0, 1.57, 0.5))
    print("moving...")
    time.sleep(50) # Adjust as needed
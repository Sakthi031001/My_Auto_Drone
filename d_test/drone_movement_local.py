import time
from pymavlink import mavutil
from general.conn import master

def d_mov_loc():
    master.wait_heartbeat()

    print("Target Sustem : ",master.target_system, "Target_Component : ", master.target_component)

    x = float(input("Position in x (positive for North) : "))
    y = float(input("Position in y (positive for East) : "))
    z = float(input("Position in z (positive for Down) : "))


    master.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(10, master.target_system,
                            master.target_component, mavutil.mavlink.MAV_FRAME_LOCAL_NED, int(0b010111111000), x, y, z, 0, 0, 0, 0, 0, 0, 1.7, 0.5))


    # Fly to a waypoint (replace coordinates with your desired waypoint)

    #master.mav.send(mavutil.mavlink.MAVLink_set_position_target_global_int_message(10, master.target_system,
    #                        master.target_component, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, int(0b110111111000), int(-35.3632260 * 10 ** 7), int(149.1622567 * 10 ** 7), 
    #                        10, 0, 0, 0, 0, 0, 0, 1.57, 0.5))
    print("moving...")
#time.sleep(50) # Adjust as needed

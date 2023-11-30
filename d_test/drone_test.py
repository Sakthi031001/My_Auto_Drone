import time
from pymavlink import mavutil
from general.conn import master


class drone_control:
    
    def d_arm():
        # changing to guided mode
        master.set_mode(4)

        # Arm the vehicle
        master.arducopter_arm()

        print("The vehicle is ARMED...")

    def d_takeoff():
        # changing to guided mode
        master.set_mode(4)

        # Arm the vehicle
        master.arducopter_arm()

        alt = float(input("Enter the altitude : "))

        # Take off to an altitude of 10 meters
        print("Taking off...")
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            alt
        )

        # Wait for takeoff to complete
        time.sleep(15)  # Adjust as needed
        print("Reached altitude...")

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

    def d_rtl():
        #setting mode to rtl
        master.set_mode(6)
        time.sleep(20)
        print("Landing...")


    def d_disarm():
        # Disarm the vehicle
        print("Disarming...")
        master.arducopter_disarm()

    def d_land():
        # Settng mode to land
        master.set_mode(9)

    def d_m_auto():
        # changing to guided mode
        master.set_mode(3)

        print("Mode changed to AUTO")
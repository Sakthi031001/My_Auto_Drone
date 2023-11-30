import time
from pymavlink import mavutil
from general.conn import master


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
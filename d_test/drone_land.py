import time
from pymavlink import mavutil
from general.conn import master

#changing mode to RTL
def d_land():
    master.set_mode(6)
    time.sleep(20)
    print("Landing...")
# Land the vehicle



"""master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_LAND,
    0,
    0,
    0,
    0,
    0,
    0,
    -35.3633439,  # Latitude of the waypoint
    149.1652396,  # Longitude of the waypoint
    0             # Altitude of the waypoint
)

# Wait for landing to complete
time.sleep(10)  # Adjust as needed"""

# Disarm the vehicle
print("Disarming...")
master.arducopter_disarm()

print("Mission complete.")
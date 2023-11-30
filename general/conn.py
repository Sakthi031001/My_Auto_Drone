import time
from pymavlink import mavutil

# Connect to mavproxy (replace '127.0.0.1:5760' with your vehicle's address)
master = mavutil.mavlink_connection('tcp:127.0.0.1:5763')
from d_test.drone_test import drone_control as dc

comment = """To arm test enter 1
                To arm and takeoff enter 2
                To move with X, Y and Z axis enter 3
                To move globally enter 4
                To land enter 5
                To RTL enter 6
                To Auto enter 7"""

print(comment)

def switch(num):
    if num == 1:
        dc.d_arm()
    elif num ==2:
        dc.d_takeoff()
    elif num ==3:
        dc.d_mov_loc()
    elif num == 4:
        dc.d_mov_glo()
    elif num == 5:
        dc.d_land()
    elif num == 6:
        dc.d_rtl()
    elif num == 7:
        dc.d_m_auto()
    else:
        print("enter a valid number!")

num = 1
while(num != 0):
    switch(num)
    print(comment)
    num = int(input("enter the mode : "))
print("done..")
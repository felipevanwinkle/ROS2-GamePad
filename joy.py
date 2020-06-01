from inputs import devices
from inputs import get_gamepad
infile_path = "/dev/input/js0"

for device in devices:
    print(device)

def color_buttons():
    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == 'BTN_SOUTH' and event.state == 1:
                print("\"A\" was pressed")
            elif event.code == 'BTN_NORTH' and event.state == 1:
                print("\"Y\" was pressed")
            elif event.code == 'BTN_EAST' and event.state == 1:
                print("\"B\" was pressed")
            elif event.code == 'BTN_WEST' and event.state == 1:
                print("\"X\" was pressed")

def triggers():
   while 1:
        events = get_gamepad()
        for event in events:
            #print(event.code, event.state)
            #number = str(event.state)
            floating = float((event.state - 23) /10)
            rounding = round(floating, 2)
            if event.code == 'ABS_RZ' and event.state > 0:
                print("\"Right trigger\" was pressed ")
                print(rounding)
            elif event.code == 'ABS_Z' and event.state > 0:
                print("\"Left trigger\" was pressed ")
                print(rounding)

def nubs():
    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == 'BTN_TL' and event.state == 1:
                print("\"LB\" was pressed")
            elif event.code == "BTN_TR" and event.state == 1:
                print("\"RB\" was pressed")

def dpad():
    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == "ABS_HAT0X" and event.state == 1:
                print("\"Right\" of the d-pad was pressed")
            elif event.code == "ABS_HAT0X" and event.state == -1:
                print("\"Left\" of the d-pad was pressed")
            elif event.code == "ABS_HAT0Y" and event.state == -1:
                print("\"Up\" of the d-pad was pressed")
            elif event.code == "ABS_HAT0Y" and event.state == 1:
                print("\"Down\" of the d-pad was pressed")

def joy_sticks():
    while 1:
        events = get_gamepad()
        for event in events:
            number = str(event.state)
            if event.code == "ABS_RY" and event.state < 0:
                print("Right joy stick up and right " + number)
            elif event.code == "ABS_RY" and event.state > 0:
                print("Right joy stick down and left " + number)
            elif event.code ==  "ABS_Y" and event.state > 0:
                print("Left joy stick " + number )
            elif event.code == "Y" and event.state < 0:
                print("Left joy stick " + number)

def misc():
    while 1:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_SELECT" and event.state == 1:
                print("\"Change View\" was pressed")
            elif event.code == "BTN_START" and event.state == 1:
                print("\"Menu\" was pressed")
            elif event.code == "BTN_MODE" and event.state == 1:
                print("\"Xbox Home\" was pressed")

def main():
    color_buttons()
    triggers()
    nubs()
    dpad()
    joy_sticks()
    misc()
    


main()

        
                
                
        
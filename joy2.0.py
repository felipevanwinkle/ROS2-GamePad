import os
from inputs import devices
from inputs import get_gamepad
infile_path = "/dev/input/js0"

    
def functions():
    print('Ala Engineering 2020')
    print('')
    #print('1.Colorful Buttons (A.)\n2.Triggers (B.)\n3.Nubs (X.)\n4.Dpad (Y.)\n5.Miscellaneous (LB.)\n6.Joysticks (RB.)') 
    print('1.Colorful Buttons \n2.Triggers \n3.Nubs \n4.Dpad \n5.Miscellaneous \n6.Joysticks\n ') 
    val = input('Choose a number to see specific functionality of the controller: ')
    os.system('clear')
    if val == '1':
        print('Colorful Buttons \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
        while 1:
            events = get_gamepad()
            for event in events:
                if event.code == 'BTN_SOUTH' and event.state == 1 or event.code == 'BTN_SOUTH' and event.state == 0:
                    button_a = (event.state)
                    print('A:' + str(button_a) + ' B:0 X:0 Y:0', end='\r')
                elif event.code == 'BTN_EAST' and event.state == 1 or event.code == 'BTN_EAST' and event.state == 0:
                    button_b = (event.state)
                    print('A:0 B:' + str(button_b) + ' X:0 Y:0', end='\r')
                elif event.code == 'BTN_NORTH' and event.state == 1 or event.code == 'BTN_NORTH' and event.state == 0:
                    button_x = (event.state)
                    print('A:0 B:0 X:' + str(button_x) + ' Y:0', end='\r')
                elif event.code == 'BTN_WEST' and event.state == 1 or event.code == 'BTN_WEST' and event.state == 0:
                    button_y = (event.state)
                    print('A:0 B:0 X:0 Y:' + str(button_y), end='\r')
                elif event.code == "BTN_MODE" and event.state == 1:
                    os.system('clear')
                    functions()
    elif val == '2':
        print('Triggers \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
        while 1:
            events = get_gamepad()
            for event in events:
                floating = float((event.state - 23) /10)
                value = round(floating, 2)
                minimum_value = -0.0
                if event.code == 'ABS_RZ' and event.state > 0:
                    print('LT:0     RT:' + str(value), end='\r')
                    if minimum_value > event.state:
                        print('LT:0     RT:0', end='\r')
                elif event.code == 'ABS_Z' and event.state > 0:
                    print('LT:' + str(value) + '     RT:0', end='\r')
                elif event.code == "BTN_MODE" and event.state == 1:
                    os.system('clear')
                    functions()
    elif val == '3':
        print('Nubs \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
        while 1:
            events = get_gamepad()
            for event in events:
                if event.code == 'BTN_TL' and event.state == 1 or event.code == 'BTN_TL' and event.state == 0:
                    lb_value = (event.state)
                    print('LB:' + str(lb_value) + ' RB:0', end='\r')
                elif event.code == "BTN_TR" and event.state == 1 or event.code == "BTN_TR" and event.state == 0:
                    rb_value = (event.state)
                    print('LB:0 RB:' + str(rb_value), end='\r')
                elif event.code == "BTN_MODE" and event.state == 1:
                    os.system('clear')
                    functions()
    elif val == '4':
        print('Dpad \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
        while 1:
            events = get_gamepad()
            for event in events:
                if event.code == "ABS_HAT0X" and event.state == 1 or event.code == "ABS_HAT0X" and event.state == 0:
                    rdpad = (event.state)
                    print('Up:0  Down:0  Right:' + str(rdpad) + '  Left:0', end='\r')       
                elif event.code == "ABS_HAT0X" and event.state == -1 or event.code == "ABS_HAT0X" and event.state == 0:
                    ldpad = (event.state)
                    print('Up:0  Down:0  Right:0  Left:' + str(ldpad), end='\r')
                elif event.code == "ABS_HAT0Y" and event.state == -1 or event.code == "ABS_HAT0Y" and event.state == 0:
                    udpad = (event.state)
                    print('Up:' + str(udpad) + '  Down:0  Right:0  Left:0', end='\r')       
                elif event.code == "ABS_HAT0Y" and event.state == 1 or event.code == "ABS_HAT0Y" and event.state == 0:
                    ddpad = (event.state)
                    print('Up:0  Down:' + str(ddpad) + ' Right:0  Left:', end='\r')
                elif event.code == "BTN_MODE" and event.state == 1:
                    os.system('clear')
                    functions()
    elif val == '5':
        print('Miscellaneous \n(i.e. to go back to the menu press the \"B Button\")')
        while 1:
            events = get_gamepad()
            for event in events:
                if event.code == "BTN_SELECT" and event.state == 1 or event.code == "BTN_SELECT" and event.state == 0:
                    select = (event.state)
                    print('Select:'+ str(select) +' Start:0 Home:0', end='\r')
                elif event.code == "BTN_START" and event.state == 1 or event.code == "BTN_START" and event.state == 0:
                    start = (event.state)
                    print('Select:0 Start:'+ str(start) +' Home:0', end='\r')
                elif event.code == "BTN_MODE" and event.state == 1 or event.code == "BTN_MODE" and event.state == 0:
                    home = (event.state)
                    print('Select:0 Start:0 Home:' + str(home), end='\r')
                elif event.code == 'BTN_EAST' and event.state == 1 or event.code == 'BTN_EAST' and event.state == 0:
                    os.system('clear')
                    functions()
    elif val == '6':
        print('Joystick \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
        while 1:
            events = get_gamepad()
            for event in events:
                joystick_value = str(event.state)
                if event.code == "ABS_RY" and event.state < 0:
                    print("Right joy stick right or up " + joystick_value, end='\r')
                elif event.code == "ABS_RY" and event.state > 0:
                    print("Right joy stick down or left " + joystick_value, end='\r')
                elif event.code ==  "ABS_Y" and event.state > 0:
                    print("Left joy stick down or right " + joystick_value, end='\r')
                elif event.code == "ABS_Y" and event.state < 0:
                    print("Left joy stick up or left " + joystick_value, end='\r')
                elif event.code == "BTN_MODE" and event.state == 1:
                    os.system('clear')
                    functions()
                

def main():
    functions()


main()


    
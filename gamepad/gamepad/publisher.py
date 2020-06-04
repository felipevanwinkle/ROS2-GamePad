import rclpy, os
from rclpy.node import Node
from std_msgs.msg import String
from inputs import devices
from inputs import get_gamepad
infile_path = "/dev/input/js0"


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'events', 10) 
        self.xbox_controller()

    def xbox_controller(self):
        print('AlA')
        print('')
        print('1.Colorful Buttons \n2.Triggers \n3.Nubs \n4.Dpad \n5.Miscellaneous \n6.Joysticks\n ') 
        self.val = input('Choose a number to see specific functionality of the controller: ')
        os.system('clear')
        if self.val == '1':
            print('Colorful Buttons \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
            while 1:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_RY' or event.code == 'ABS_Y':
                        continue
                    if event.code == 'BTN_SOUTH' or event.code == 'BTN_EAST' or event.code == 'BTN_NORTH' or event.code == 'BTN_WEST' or event.code == 'BTN_MODE' or event.code == 'SYN_REPORT' or event.code == 'ABS_X' or event.code == 'ABS_RX':
                        if event.code == 'BTN_SOUTH' and event.state == 1 or event.code == 'BTN_SOUTH' and event.state == 0:
                            self.button_a = ('A:' + str(event.state) + ' B:0 X:0 Y:0')
                            msg = String()
                            msg.data = str(self.button_a)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_EAST' and event.state == 1 or event.code == 'BTN_EAST' and event.state == 0:
                            self.button_b = ('A:0 B:' + str(event.state) + ' X:0 Y:0')
                            msg = String()
                            msg.data = str(self.button_b)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_NORTH' and event.state == 1 or event.code == 'BTN_NORTH' and event.state == 0:
                            self.button_x = ('A:0 B:0 X:' + str(event.state) + ' Y:0')
                            msg = String()
                            msg.data = str(self.button_x)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_WEST' and event.state == 1 or event.code == 'BTN_WEST' and event.state == 0:
                            self.button_y = ('A:0 B:0 X:0 Y:' + str(event.state))
                            msg = String()
                            msg.data = str(self.button_y)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_MODE' and event.state == 1:
                            os.system('clear')
                            self.xbox_controller()  
                    else:
                        print('Invalid Syntax: A,B,X,Y Only')
                    
        elif self.val == '2':
            print('Triggers \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
            while 1:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_RY' or event.code == 'ABS_Y':
                        continue
                    if event.code == 'ABS_RZ' or event.code == 'ABS_Z' or event.code == 'BTN_MODE' or event.code == 'SYN_REPORT' or event.code == 'ABS_X' or event.code == 'ABS_RX':
                        self.floating = float((event.state - 23) /10)
                        self.value = round(self.floating, 2)
                        if event.code == 'ABS_RZ' and event.state > 0:
                            self.rt_layout = ('LT:0     RT:' + str(self.value))
                            msg = String()
                            msg.data = str(self.rt_layout)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'ABS_Z' and event.state > 0:
                            self.lt_layout = ('LT:' + str(self.value) + '  RT:0')
                            msg = String()
                            msg.data = str(self.lt_layout)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_MODE' and event.state == 1:
                            os.system('clear')
                            self.xbox_controller()()
                    else:
                        print('Invalid Syntax: RT,LT Only')

        elif self.val == '3':
            print('Nubs \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
            while 1:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_RY' or event.code == 'ABS_Y':
                        continue
                    if event.code == 'BTN_TL' or event.code == 'BTN_TR' or event.code == 'BTN_MODE' or event.code == 'SYN_REPORT' or event.code == 'ABS_X' or event.code == 'ABS_RX':
                        if event.code == 'BTN_TL' and event.state == 1 or event.code == 'BTN_TL' and event.state == 0:
                            self.lb_value = ('LB:' + str(event.state) + ' RB:0')
                            msg = String()
                            msg.data = str(self.lb_value)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_TR' and event.state == 1 or event.code == 'BTN_TR' and event.state == 0:
                            self.rb_value = ('LB:0 RB:' + str(event.state))
                            msg = String()
                            msg.data = str(self.rb_value)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_MODE' and event.state == 1:
                            os.system('clear')
                            self.xbox_controller()
                    else:
                        print('Invalid Syntax: LB,RB Only')

        elif self.val == '4':
            print('Dpad \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
            while 1:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_RY' or event.code == 'ABS_Y':
                        continue
                    if event.code == 'ABS_HAT0X' or event.code == 'ABS_HAT0Y' or event.code == 'BTN_MODE' or event.code == 'SYN_REPORT' or event.code == 'ABS_X' or event.code == 'ABS_RX':
                        if event.code == 'ABS_HAT0X' and event.state == 1 or event.code == 'ABS_HAT0X' and event.state == 0:
                            self.rdpad = ('Up:0  Down:0  Right:' + str(event.state) + '  Left:0')
                            msg = String()
                            msg.data = str(self.rdpad)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)     
                        elif event.code == 'ABS_HAT0X' and event.state == -1 or event.code == 'ABS_HAT0X' and event.state == 0:
                            self.ldpad = ('Up:0  Down:0  Right:0  Left:' + str(event.state))
                            msg = String()
                            msg.data = str(self.ldpad)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'ABS_HAT0Y' and event.state == -1 or event.code == 'ABS_HAT0Y' and event.state == 0:
                            self.udpad = ('Up:' + str(event.state) + '  Down:0  Right:0  Left:0')
                            msg = String()
                            msg.data = str(self.udpad)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)      
                        elif event.code == 'ABS_HAT0Y' and event.state == 1 or event.code == 'ABS_HAT0Y' and event.state == 0:
                            self.ddpad = ('Up:0  Down:' + str(event.state) + ' Right:0  Left:')
                            msg = String()
                            msg.data = str(self.ddpad)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_MODE' and event.state == 1:
                            os.system('clear')
                            self.xbox_controller()
                    else:
                        print('Invalid Syntax: Up,Down,Right,Left of the Dpad Only')
                        
        elif self.val == '5':
            print('Miscellaneous \n(i.e. to go back to the menu press the \"B Button\")')
            while 1:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_RY' or event.code == 'ABS_Y':
                        continue
                    if event.code == 'BTN_START' or event.code == 'BTN_SELECT' or event.code == 'BTN_EAST' or event.code == 'BTN_MODE' or event.code == 'SYN_REPORT' or event.code == 'ABS_X' or event.code == 'ABS_RX':
                        if event.code == "BTN_SELECT" and event.state == 1 or event.code == "BTN_SELECT" and event.state == 0:
                            self.select = ('Select:'+ str(event.state) +' Start:0 Home:0')
                            msg = String()
                            msg.data = str(self.select)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_START' and event.state == 1 or event.code == 'BTN_START' and event.state == 0:
                            self.start = ('Select:0 Start:'+ str(event.state) +' Home:0')
                            msg = String()
                            msg.data = str(self.start)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_MODE' and event.state == 1 or event.code == 'BTN_MODE' and event.state == 0:
                            self.home = ('Select:0 Start:0 Home:' + str(event.state))
                            msg = String()
                            msg.data = str(self.home)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_EAST' and event.state == 1 or event.code == 'BTN_EAST' and event.state == 0:
                            os.system('clear')
                            self.xbox_controller()
                    else:
                        print('Invalid Syntax: Select,Start,Home Only')

        elif self.val == '6':
            print('Joystick \n(i.e. to go back to the menu press the \"Xbox Home Button\")')
            while 1:
                events = get_gamepad()
                for event in events:
                    if event.code == 'ABS_RY' or event.code == 'ABS_Y' or event.code == 'BTN_MODE' or event.code == 'SYN_REPORT' or event.code == 'ABS_X' or event.code == 'ABS_RX':
                        self.joystick_value = str(event.state)
                        if event.code == 'ABS_RY' and event.state < 0:
                            self.location = ('Right joy stick left or up ' + self.joystick_value)
                            msg = String()
                            msg.data = str(self.location)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'ABS_RY' and event.state > 0:
                            self.location = ('Right joy stick down or right ' + self.joystick_value)
                            msg = String()
                            msg.data = str(self.location)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code ==  'ABS_Y' and event.state > 0:
                            self.location = ('Left joy stick down or right ' + self.joystick_value)
                            msg = String()
                            msg.data = str(self.location)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'ABS_Y' and event.state < 0:
                            self.location = ('Left joy stick up or left ' + self.joystick_value)
                            msg = String()
                            msg.data = str(self.location)
                            self.publisher_.publish(msg)
                            self.get_logger().info(msg.data)
                        elif event.code == 'BTN_MODE' and event.state == 1:
                            os.system('clear')
                            self.xbox_controller()
                    else:
                        print('Invalid Syntax: Left & Right Joystick Only')
                
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String,'abxy',self.colorfulbuttons_callback,10)
        self.subscription = self.create_subscription(String, 'lt/rt',self.triggers_callback,10)
        self.subscription = self.create_subscription(String, 'lb/rb',self.nubs_callback,10)
        self.subscription = self.create_subscription(String, 'dpad',self.dpad_callback,10)
        self.subscription = self.create_subscription(String, 'misc',self.misc_callback,10)
        self.subscription = self.create_subscription(String, 'analog',self.analog_callback,10)
        self.subscription 

    def colorfulbuttons_callback(self, msg):
        self.get_logger().info('Current Value: "%s"' % msg.data)

    def triggers_callback(self, msg_triggers):
        self.get_logger().info('Percentile Value: "%s"' % msg_triggers.data)

    def nubs_callback(self, msg_nubs):
        self.get_logger().info('Current Value: "%s"' % msg_nubs.data)

    def dpad_callback(self, msg_dpad):
        self.get_logger().info('Current Value: "%s"' % msg_dpad.data)

    def misc_callback(self, msg_misc):
        self.get_logger().info('Current Value: "%s"' % msg_misc.data)

    def analog_callback(self, msg_joy):
        self.get_logger().info('Current Value: "%s"' % msg_joy.data)


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
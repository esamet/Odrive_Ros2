import rclpy
from rclpy.node import Node
import odrive
my_drive=odrive.find_any(serial_number="2057387D3952")
my_drive2=odrive.find_any(serial_number="206437A15853")
from geometry_msgs.msg import Twist


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.subscription = self.create_subscription(Twist, '/cmd_vel',self.listener_callback, 10)
        timer_period = 0.5  # seconds
        self.subscription
        
        

    def listener_callback(self, msg):
        
        

        _linear_x= msg.linear.x
        print(msg.linear.x)
        my_drive.axis0.controller.input_vel = _linear_x
        my_drive.axis1.controller.input_vel = _linear_x
        my_drive2.axis1.controller.input_vel = _linear_x
        my_drive2.axis1.controller.input_vel = _linear_x

        self.get_logger().info('Publishing: "%s"  ' % _linear_x)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
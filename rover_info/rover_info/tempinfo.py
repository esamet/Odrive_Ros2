import rclpy
from rclpy.node import Node
import odrive
my_drive=odrive.find_any()
from std_msgs.msg import Float32MultiArray


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, '/Odrv_Temperature', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float32MultiArray()
        voltage_info= my_drive.axis0.fet_thermistor.temperature
        voltage_info2= my_drive.axis0.fet_thermistor.temperature
        msg.data = [voltage_info,voltage_info2]
        print(msg.data)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data[0])
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
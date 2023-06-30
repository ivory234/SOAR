import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from senser_msgs.msg import Image
import numpy as np
import cv2 as cv
import cv_bridge import CvBridge

class ImageSub(Node):
    def __init__(self):
        super().__init__('image_sub')
        qos = QoSProfile(depth=10)
        self.image_sub = self.create_subscription(
            Image,
            'zed2/zed_node',
            self.image_callback,
            qos)
        self.image = np.empty(shape=[1])
        
    def image_callback(self, data):
        self.image = bridge.imgmsg_to_cv2(data, 'bgr8')
        cv.imshow('img', self.image)
        cv.waitKey(33)
        
def main(args=None):
    rclpy.init(args=args)
    node = ImageSubscriber()
    
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        node.get_logger.info('Stopped by Keyboard')
    finally :
        node.destory_node()
        rclpy.shutdown()

if __name__ == '__main__'    :
    main()

        
    
    
    
    
        
    
        






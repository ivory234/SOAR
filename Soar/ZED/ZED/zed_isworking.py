
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
import numpy as np
 
class ImageSubscriber(Node):
 
  def __init__(self):
    
    super().__init__('isworking')
      
    self.subscription = self.create_subscription(
      Image, 
      '/zed2/zed_node/rgb_raw/image_raw_color',
      self.listener_callback, 
      10)
    self.subscription 
      
    self.br = CvBridge()
   
  def listener_callback(self, data):

    self.get_logger().info('isworking')
    
def main(args=None):
  
  rclpy.init(args=args)
  
  image_subscriber = ImageSubscriber()
  
  rclpy.spin(image_subscriber)

  image_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()

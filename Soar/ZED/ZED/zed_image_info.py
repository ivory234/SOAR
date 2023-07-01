
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
import numpy as np
 
class ImageSubscriber(Node):
 
  def __init__(self):
    
    super().__init__('image_info')
      
    self.subscription = self.create_subscription(
      Image, 
      '/zed2/zed_node/rgb_raw/image_raw_color',
      self.listener_callback, 
      10)
    self.subscription 
      
    self.br = CvBridge()
   
  def listener_callback(self, data):

    self.get_logger().info('isworking')
    current_frame = self.br.imgmsg_to_cv2(data)
    
    
    fheight, fwidth, fchannel = current_frame.shape
    
    # 변환이미지 속성
    self.get_logger().info('data.height = {0}'.format(data.height))
    self.get_logger().info('data.height = {0}'.format(data.width))   
    self.get_logger().info('transformed - height : {0} | width :  {1} | channel : {2}'.format(fheight, fwidth, fchannel))
    
    '''
    sensor_msgs/Image 
    
    height
    width
    encoding
    bigendian
    step
    data
 
    '''
    
    
    
def main(args=None):
  
  rclpy.init(args=args)
  
  image_subscriber = ImageSubscriber()
  
  rclpy.spin(image_subscriber)

  image_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()

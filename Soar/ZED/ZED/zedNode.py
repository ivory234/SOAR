
import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
 
class ImageSubscriber(Node):
 
  def __init__(self):
    
    super().__init__('image_subscriber')
      
    self.subscription = self.create_subscription(
      Image, 
      self.listener_callback, 
      10)
    self.subscription 
      
    self.br = CvBridge()
   
  def listener_callback(self, data):

    current_frame = self.br.imgmsg_to_cv2(data)
    
    height, width, channel = data.shape
    fheight, fwidth, fchannel = current_frame.shape
    
    self.get_logger().info('--------------------')
    # data 속성
    self.get_logger().info(data)
    self.get_logger().info(data.size)
    self.get_logger().info(data.dtype)
    
    # 변환이미지 속성
    self.get_logger().info('height : %d | width :  %d | channel : %d', height, width, channel)
    self.get_logger().info(current_frame.size)
    self.get_logger().info(current_frame.dtype)
    
    
  
def main(args=None):
  
  rclpy.init(args=args)
  
  image_subscriber = ImageSubscriber()
  
  rclpy.spin(image_subscriber)

  image_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
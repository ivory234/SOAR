import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from senser_msgs.msg import Image


from rcl.qos import QoSProfile
from rcply.qos import QoSDurabilityPolicy as qd
from rcply.qos import QoSHistoryPolicy as qh
from rcply.qos import QoSReliabilityPolicy as qr

import numpy as np
import cv2 as cv
import cv_bridge import CvBridge

class ImageSub(Node):
    def __init__(self):
        super().__init__('image_sub')
        
        QoS_depth = QoSProfile(
            reliability = qr.BEST_EFFORT,   # 데이터 전송 옵션 : 전송속도 > 신뢰성
            history = qh.KEEP_LAST,   # 데이터 보관 : 정해진 depth만을 보관 > 모든 데이터 보관
            durability = qd.VOLATILE,   # 서브스크라이버 생성전 데이터 : 보관 < 무효
            depth = 10
        )
        self.image_sub = self.create_subscription(
            Image,
            'zed2/zed_node/stereo_raw/image_raw_color',
            self.image_callback(msg[0]),
            QoS_depth)
        self.image = np.empty(shape=[1])
        
    def image_callback(self, data):
        self.image = bridge.imgmsg_to_cv2(data, 'bgr8')
        cv.imshow('img', self.image)
        cv.waitKey(33)
        
def main(args=None):
    rclpy.init(args=args)
    node = ImageSub()
    
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        node.get_logger.info('Stopped by Keyboard')
    finally :
        node.destory_node()
        rclpy.shutdown()

if __name__ == '__main__'    :
    main()

        
    
    
    
    
        
    
        






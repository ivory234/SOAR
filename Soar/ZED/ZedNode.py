import rclpy
from rclpy.node import Node

from rcl.qos import QoSProfile
from rcply.qos import QoSDurabilityPolicy as qd
from rcply.qos import QoSHistoryPolicy as qh
from rcply.qos import QoSReliabilityPolicy as qr


from std_msgs.msg import String
from sensor_msg.msg import Image
from sensor_msg.msg import PointCloud2
from sensor_msg.msg import CameraInfo


import droneflag as df


class DepthSub(Node):
    def __init__(self):
        super().__init__('zed_depth')
        
        QoS_depth = QoSProfile(
            reliability = qr.BEST_EFFORT,   # 데이터 전송 옵션 : 전송속도 > 신뢰성
            history = qh.KEEP_LAST,   # 데이터 보관 : 정해진 depth만을 보관 > 모든 데이터 보관
            durability = qd.VOLATILE,   # 서브스크라이버 생성전 데이터 : 보관 < 무효
            depth = 10
        )
                
        self.depth
        self.depth_width
        self.depth_height
        
        self.depthSub = self.create_subscription(Image, 'depth', QoS_depth, self.depthCallback)

    def depthCallback(self, msg):
        self.get_logger().info('sensing depth : %d | width : %d | height : %d', 
                               msg.data[0], msg.width, msg.height)
        
        # 받은 depth 이미지 (아마도 배열)
        self.depths = msg.data[0]
        
        # 받은 depth 이미지의
        self.depth_width = msg.width
        self.depth_height = msg.heigt
        
'''
class VideoSub(Node):
    def __init__(self):
        super().__init__('zed_video')
        
        QoS_depth = QoSProfile(
            reliability = qr.BEST_EFFORT,   # 데이터 전송 옵션 : 전송속도 > 신뢰성
            history = qh.KEEP_LAST,   # 데이터 보관 : 정해진 depth만을 보관 > 모든 데이터 보관
            durability = qd.VOLATILE,   # 서브스크라이버 생성전 데이터 : 보관 < 무효
            depth = 10
        )
                
        self.depth
        self.depth_width
        self.depth_height
        
        self.depthSub = self.create_subscription(Image, 'depth', QoS_depth, self.depthCallback)

    def depthCallback(self, msg):
        self.get_logger().info('sensing depth : %d | width : %d | height : %d', 
                               msg.data[0], msg.width, msg.height)
        
        # 받은 depth 이미지 (아마도 배열)
        self.depths = msg.data[0]
        
        # 받은 depth 이미지의
        self.depth_width = msg.width
        self.depth_height = msg.heigt
        
class Zed_CameraInfoSub(Node):
    def __init__(self):
        super().__init__('zed_cameraIn')
'''
        
'''
class yoloPub(Node):
    
    def __init__(self):
        super().__init__('yolo_pub')
        qos_profile = QoSProfile(depth=10)
        self.publisher = self.create_publisher(Image, 'yolo_pub' qos_profile)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        def timer_callback(self):
            msg = Image()
            msg.data = 
            
'''
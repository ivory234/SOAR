import rclpy
from rclpy.node import Node

from rclpy.qos import QoSProfile
from rclpy.qos import QoSDurabilityPolicy as qd
from rclpy.qos import QoSHistoryPolicy as qh
from rclpy.qos import QoSReliabilityPolicy as qr
import struct
import numpy as np
import math
from geometry_msgs.msg import Point

yaw = 1.5704

def zed_world_frame_2_NED_frame(zed_world_x,zed_world_y,zed_world_z,yaw):
    zed_world_coordinate = np.array([[zed_world_x],[zed_world_y],[zed_world_z]])
    zed_world_2_NED_world_rotation_matrix = np.array(
       [
       [math.sin(yaw),math.cos(yaw),0],
       [0,0,1],
       [math.cos(yaw),math.sin(yaw)* -1,0]
        ])
    NED_coordinate = zed_world_2_NED_world_rotation_matrix @ zed_world_coordinate
    NED_x = NED_coordinate[0]
    NED_y = NED_coordinate[1]
    NED_z = NED_coordinate[2]
    
    print("NED_x_coordinate : ", NED_x)
    print("NED_y_coordinate : ", NED_y)
    print("NED_z_coordinate : ", NED_z)

class s2s_subscription_Node(Node):

    def __init__(self):
        super().__init__('s2s_sub_Node')

        self.subscriber_s2s_result = self.create_subscription(Point, 's2s_result', self.callback_s2s_result, 10)

    def callback_s2s_result(self,msg):
        world_x = msg.x
        world_y = msg.y
        world_z = msg.z

        zed_world_frame_2_NED_frame(world_x,world_y,world_z,yaw)

        
def main(args=None):
 
  rclpy.init(args=args)
  
  s2s_result_subscriber = s2s_subscription_Node()
  
  rclpy.spin(s2s_result_subscriber)

  s2s_result_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()




  
import rclpy
from rclpy.node import Node

from rclpy.qos import QoSProfile
from rclpy.qos import QoSDurabilityPolicy as qd
from rclpy.qos import QoSHistoryPolicy as qh
from rclpy.qos import QoSReliabilityPolicy as qr
import struct
import numpy as np
# import calc

from geometry_msgs.msg import Point
from sensor_msgs.msg import PointCloud2
from geometry_msgs.msg import PoseStamped
#from vision_msgs import Detection2DArray

#from message_filters import ApproximateTimeSynchronizer, Subscriber

zed_pixel_x = 896
zed_pixel_y = 512

def Q2M(q0,q1,q2,q3):
            # First row of the rotation matrix
            r00 = - 2 * (q2 * q2 + q3 * q3) + 1
            r01 = 2 * (q1 * q2 - q0 * q3)
            r02 = 2 * (q1 * q3 + q0 * q2)
            # Second row of the rotation matrix
            r10 = 2 * (q1 * q2 + q0 * q3)
            r11 = - 2 * (q1 * q1 + q3 * q3) + 1
            r12 = 2 * (q2 * q3 - q0 * q1)
            # Third row of the rotation matrix
            r20 = 2 * (q1 * q3 - q0 * q2)
            r21 = 2 * (q2 * q3 + q0 * q1)
            r22 = - 2 * (q1 * q1 + q2 * q2) + 1
        
            # 3x3 rotation matrix
            rot_matrix = np.array([[r00, r01, r02],
                                   [r10, r11, r12],
                                   [r20, r21, r22]])
                                
            return rot_matrix
        
def Transform(rotation_matrix, cx_point, cy_point, cz_point, tx, ty, tz):
    
    result = np.zeros((1,3)) 
    point = np.array([[cx_point], [cy_point], [cz_point]])
    tr = np.array([[tx], [ty], [tz]])
    
    result = rotation_matrix @ point + tr
    return result
    
def pointcloud_converter(x1,x2,x3,x4):
    
    point_cloud_x_data:list = [x1,x2,x3,x4]

    x_data_int:int = (point_cloud_x_data[3] << 24 | point_cloud_x_data[2] << 16 | point_cloud_x_data[1] << 8 | point_cloud_x_data[0])
    x_data_bin_str:str = bin(x_data_int)[2:].zfill(32)
    x_data_bin:bytes = int(x_data_bin_str,2)
    point_value = struct.unpack('f', struct.pack('I', x_data_bin))[0]

    return point_value 
    
def find_index_from_yolo_information(zed_x_pixel,yolo_x,yolo_y):
    index = ((yolo_y-1) * zed_x_pixel + yolo_x - 1) * 16  
    return index

def find_xyz_from_index(array, index):
      
      output_array = []
      x_output_array = array[index:index+4]
      y_output_array = array[index+4:index+8]
      z_output_array = array[index+8:index+12]

      return x_output_array, y_output_array, z_output_array


class s2s_Node(Node):

    def __init__(self):
        super().__init__('s2s_Node')

        #self.yolo_msg
        #self.pose_msg = None
        #self.pointCloud2_msg = None


        self.sync_yolo = -1
        self.sync_pose = -1
        self.sync_pointCloud2 = -1
        self.sync_pose_flag = -1

        self.T = np.array([[0],[0],[0]])

        
        self.xa= np.array([0,0,0,0])
        self.ya= np.array([0,0,0,0])
        self.za= np.array([0,0,0,0])
        
        
        # check sub
        #self.subscriber_yolo = self.create_subscription(Detection2DArray, 'soar_yolo', self.callback_yolo, 10)
        self.subscriber_pointCloud2 = self.create_subscription(PointCloud2, 'zed2/zed_node/point_cloud/cloud_registered', self.callback_pointCloud2, 10)
        self.subscriber_pose = self.create_subscription(PoseStamped, 'zed2/zed_node/pose', self.callback_pose, 10)
        
        self.s2s_result = self.create_publisher(Point,'s2s_result',10)
        self.timer = self.create_timer(1.0,self.publish_s2s_result)

    #def callback_yolo(self, msg):
    #    print('[callback][yolo_topic]')
    #    self.yolo_msg = msg
    #    self.get_logger().info('[s2sNode][yolo_topic]:Get{0}'.format(self.yolo_msg))
    def publish_s2s_result(self):
        msg = Point()
        msg.x = float(self.T[0])
        msg.y = float(self.T[1])
        msg.z = float(self.T[2])
        self.s2s_result.publish(msg)

    def callback_pointCloud2(self, msg):
        
        pointCloud2_msg = msg
        self.sync_pointCloud2 = pointCloud2_msg.header.stamp.nanosec
        self.sync_pose_flag = 1
        index = find_index_from_yolo_information(
            zed_pixel_x, 
            #self.yolo_msg.bbox.center.x,
            #self.yolo_msg.bbox.center.y
            400, 250
            )
        self.xa, self.ya, self.za = find_xyz_from_index(pointCloud2_msg.data, index)


    def callback_pose(self, msg):
        
        pose_msg = msg
        self.sync_pose = pose_msg.header.stamp.nanosec
        
        if self.sync_pose_flag == 1 :
             print("[Nanosec Is Synchronize] : ", self.sync_pose)
             print('pose_time :', self.sync_pose, 'pointCloud2_time : ', self.sync_pointCloud2)
             self.sync_pose_flag = -1

             Q = Q2M(
                pose_msg.pose.orientation.w,
                pose_msg.pose.orientation.x,
                pose_msg.pose.orientation.y,
                pose_msg.pose.orientation.z
                )
        

             cx = pointcloud_converter(self.xa[0], self.xa[1], self.xa[2], self.xa[3])
             cy = pointcloud_converter(self.ya[0], self.ya[1], self.ya[2], self.ya[3])
             cz = pointcloud_converter(self.za[0], self.za[1], self.za[2], self.za[3])

        
             self.T = Transform(
                      Q,
                      cx, cy, cz,
                      pose_msg.pose.position.x,
                      pose_msg.pose.position.y,
                      pose_msg.pose.position.z,
                      )
             
             print('Final result_which_is_world_3d_coordinate: \n',self.T)
        
        # to do: make publish part 
        #       : make subscribe node of sehyun
        

def main(args=None):
 
  rclpy.init(args=args)
  
  pose_subscriber = s2s_Node()
  
  rclpy.spin(pose_subscriber)

  pose_subscriber.destroy_node()
  
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()

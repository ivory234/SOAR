# https://martinii.fun/156

import sys
import rclpy
import threading
from rclpy.node import Node
from soar_ui import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow

from sensor_msgs.msg import PointCloud2


#from px4_msgs.msg import VehicleOdometry # msg 이름 VehicleOdometry 다
from yolov8_msgs.msg import Yolov8Inference
from yolov8_msgs.msg import InferenceResult

class qtSubscriber(Node):
    def __init__(self):
        self.velocity_sub = self.create_subscription(PointCloud2, 'name', self.velocity_sub_callback, 10)
        self.velocity_sub
        self.vel_message = []

    def velocity_sub_callback(self, msg):
        self.vel_message = [msg.x, msg.y, msg.z]
class GUIUpdater(threading.Thread):
    def __init__(self, node):

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
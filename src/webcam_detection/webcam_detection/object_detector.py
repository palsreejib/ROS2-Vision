#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO

class ObjectDetector(Node):
    def __init__(self):
        super().__init__('object_detector')
        self.model = YOLO('yolov8n.pt')  # Auto-downloads on first run
        self.subscription = self.create_subscription(
            Image,
            'webcam/image_raw',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Image, 'detection/output', 10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        results = self.model(frame, imgsz=320, verbose=False)  # Optimize for laptop
        annotated_frame = results[0].plot()
        self.publisher_.publish(self.bridge.cv2_to_imgmsg(annotated_frame, 'bgr8'))

def main(args=None):
    rclpy.init(args=args)
    node = ObjectDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='webcam_detection',
            executable='webcam_publisher',
            name='webcam_publisher'
        ),
        Node(
            package='webcam_detection',
            executable='object_detector',
            name='object_detector'
        )
    ])
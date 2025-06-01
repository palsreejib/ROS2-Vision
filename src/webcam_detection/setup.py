from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'webcam_detection'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Add this line to include launch files:
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sreejib',
    maintainer_email='sreejib@todo.todo',
    description='Webcam object detection with YOLOv8',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'webcam_publisher = webcam_detection.webcam_publisher:main',
            'object_detector = webcam_detection.object_detector:main'
        ],
    },
)
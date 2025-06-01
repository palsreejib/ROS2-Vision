# ROS2-Vision

This ROS 2 (Humble) project utilizes your computer's webcam to perform real-time object detection using **YOLOv8**. The detection results can be streamed to your browser via a local web interface or through rqt.

---

## Project Structure

Only the `src/` folder is included in this repository. It contains the necessary ROS 2 packages for:

- Capturing webcam video.
- Running YOLOv8 object detection.
- Streaming annotated video through a web server or rqt.

---

### Prerequisites

- **ROS 2 Humble** installed
- **Python 3.8+**
- `ultralytics` library installed (`pip install ultralytics`)
- OpenCV (`pip install opencv-python`)
- `cv_bridge` and ROS 2 image transport packages
- A webcam connected to your system

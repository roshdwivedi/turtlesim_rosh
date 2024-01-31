This project is made possible using ROS2 and include self-created nodes with the use of external packages (e.g. usb_cam).
The goal of the project is to create an interface for controlling the robot.<br>
* Launch a camera driver (can be a laptop camera or an external camera).
* Start your node(s) to control the robot.
* Launch the robot driver.

The node created allows when the ArUco marker is detected on the screen, depending on whether the center of the marker is above the center of the erakno or below, the robot moves forward or backward.



# ❗❗Important things to consider❗❗

* Make sure ros2 is configured with humble.
* Please launch the turtlesim window first before using the main.py file.
* Make sure you are connected to a camera
* In case of a camera error please go to line 72 in main.py and make sure cv.VideoCapture(0) is set 0 (default) or customize it depending on your sytem.
## Code Components

* The script imports necessary libraries and modules, including ROS packages (rclpy, geometry_msgs, turtlesim), OpenCV (cv2), and mathematical functions (math).
* ArUco Dictionaries (ARUCO_DICT) mapping string keys to ArUco dictionary constants from OpenCV.
* Degrees to Radians Conversion is a function (degrees_radians) to convert angles from degrees to radians.
* TurtleControllerNode Class Inherits from the ROS Node class.
  * Initializes a ROS node named "turtle_controller_node."
  * Creates a publisher to control turtle movement (cmd_vel_pub_).
  * Sets up a subscriber for receiving turtle pose information (pose_subscriber_).
  * Implements a callback (pose_callback) to stop the turtle's movement when pose information is received.
* ArUco Marker Detection and Control:
  * Implements a method (detector_controller) to detect ArUco markers using a camera and control the turtle accordingly.
  * Utilizes OpenCV's ArUco functions and sets up a video capture.
  * Processes frames, detects markers, and adjusts turtle movement based on marker IDs  and Displays the processed frame and exits the loop on a keypress.
* Movement Command Publisher:
  * Implements a method (cmd_publisher) to publish movement commands to control the turtle based on detected markers.
* Main Function:
  * Initializes ROS, creates an instance of TurtleControllerNode, runs the ArUco detector, and spins the ROS node.
* Script Execution:
  * The script can be executed directly (_name_ == "_main_") to start the turtle controller node.



### Below is an image created with rqt_graph function to visualise the working of nodes
![rosgraph](https://github.com/roshdwivedi/turtlesim_rosh/assets/100048354/a484540d-1f47-484a-b31c-c6e08d69b9c5)


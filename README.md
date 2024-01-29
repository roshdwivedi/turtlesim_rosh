This project is made possible using ROS2 and include self-created nodes with the use of external packages (e.g. usb_cam).
The goal of the project is to create an interface for controlling the robot.
    1 - Launch a camera driver (can be a laptop camera or an external camera).
    2 - Start your node(s) to control the robot.
    3 - Launch the robot driver.
    4 - Demonstrate how the interface works.

The node created allows when the ArUco marker is detected on the screen, depending on whether the center of the marker is above the center of the erakno or below, the robot moves forward or backward.

The node "camera_aruco" is used to publish linear velocity of X co-ordinates for the Turtlebot. This is computed by the relative position of the boundary box of Aruco Marker.If the center of the Boundary box is in upper part of the video feed, the linear X velocity is changed due to which the turtle in window moves.

❗❗Important things to consider❗❗

Make sure ros2 is configured with humble.
Please launch the turtlesim window first before using the main.py file.
Make sure you are connected to a camera
In case of a camera error please go to line 72 in main.py and make sure cv.VideoCapture(0) is set 0 (default) or customize it depending on your sytem.

Below is an image created with rqt_graph function to visualise the working of nodes
![rosgraph](https://github.com/roshdwivedi/turtlesim_rosh/assets/100048354/a484540d-1f47-484a-b31c-c6e08d69b9c5)


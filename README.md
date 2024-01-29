This project is made possible using ROS2 and include self-created nodes with the use of external packages (e.g. usb_cam).
The goal of the project is to create an interface for controlling the robot.
    1 - Launch a camera driver (can be a laptop camera or an external camera).
    2 - Start your node(s) to control the robot.
    3 - Launch the robot driver.
    4 - Demonstrate how the interface works.

The node created allows when the ArUco marker is detected on the screen, depending on whether the center of the marker is above the center of the erakno or below, the robot moves forward or backward.

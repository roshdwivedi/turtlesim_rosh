
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import cv2 as cv
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from control_msgs.msg import JointTrajectoryControllerState
from math import pi

ARUCO_DICT = {
	"DICT_4X4_50": cv.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv.aruco.DICT_APRILTAG_36h11
}

def degrees_radians(angle_in_degrees: float):
    angle_in_radians = angle_in_degrees*pi/180
    return angle_in_radians

class TurtleControllerNode(Node):

    def __init__(self):
        super().__init__("turtle_controller_node")

        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)

        self.pose_subscriber_ = self.create_subscription(
            Pose, 
            "/turtle1/pose", 
            self.pose_callback, 
            10)
        self.get_logger().info("turtle_controller_node has been started!")

    def pose_callback(self, pose: Pose):
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.cmd_vel_pub_.publish(cmd)

    def detector_controller(self, aruco_type):
        """detect aruco markers, and controler the robot accordingly"""

        self.get_logger().info("aruco detector is running")

        aruco_dict = cv.aruco.getPredefinedDictionary(ARUCO_DICT[aruco_type])

        aruco_params = cv.aruco.DetectorParameters()

        detector = cv.aruco.ArucoDetector(aruco_dict, aruco_params)

        vid = cv.VideoCapture(0)

        vid.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
        vid.set(cv.CAP_PROP_FRAME_HEIGHT, 720)

        while vid.isOpened():
            
            ret, img = vid.read()

            h, w, _ = img.shape

            width = 1000
            height = int(width*(h/w))
            img = cv.resize(img, (width, height), interpolation=cv.INTER_CUBIC)

            markerCorners, markerIds, rejectedCandidates = detector.detectMarkers(img)

            self.cmd_publisher(markerIds)
            
            cv.aruco.drawDetectedMarkers(img, markerCorners, markerIds)

            cv.imshow("Image", img)

            key = cv.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        cv.destroyAllWindows()
        vid.release()

    def cmd_publisher(self, markerIds):
        cmd = Twist()

        if markerIds == 1:
            cmd.linear.x = 2.0
            cmd.angular.z = 1.0
        elif markerIds == 5:
            cmd.linear.x = 2.0
            cmd.angular.z = -1.0
            
        self.cmd_vel_pub_.publish(cmd)


aruco_type = "DICT_5X5_100"

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    node.detector_controller(aruco_type)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
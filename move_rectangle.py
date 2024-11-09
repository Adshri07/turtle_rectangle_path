#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import time

def move_rectangle():
    rospy.init_node('turtle_rectangle', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Define rectangle parameters (in seconds)
    forward_time = 2   # Move forward for 2 seconds
    turn_time = 1.5    # Rotate for 1.5 seconds
    rate = rospy.Rate(1)

    for _ in range(3):  # Repeat twice for a complete rectangle
        # Move forward
        vel_msg.linear.x = 2.0  # Set linear speed
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        time.sleep(forward_time)

        # Turn
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 1.57  # Approximately 90 degrees in radians per second
        velocity_publisher.publish(vel_msg)
        time.sleep(turn_time)

        # Move forward (for the length of the rectangle)
        vel_msg.linear.x = 1.0
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)
        time.sleep(forward_time)

        # Turn
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = 1.57
        velocity_publisher.publish(vel_msg)
        time.sleep(turn_time)

    # Stop the turtle after completing the rectangle
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move_rectangle()
    except rospy.ROSInterruptException:
        pass




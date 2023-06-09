#!/usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
from math import pi

if __name__ == "__main__":
    # Initialize moveit_commander and node
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('d3_move_joint_space', anonymous=False)

    # Get instance from moveit_commander
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Get group_commander from MoveGroupCommander
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)


    # Move using joint space
    joint_goal = move_group.get_current_joint_values()
    print(joint_goal)

    joint_goal[0] = 0
    joint_goal[1] = -2*pi/8
    joint_goal[2] = 0
    joint_goal[3] = -2*pi/4
    joint_goal[4] = 0
    joint_goal[5] = 2*pi/6
    joint_goal[6] = 0


    move_group.go(joint_goal, wait=True)
    move_group.stop()

    current_joints = move_group.get_current_joint_values()
    print(current_joints)

    quit()

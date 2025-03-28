#!/usr/bin/env python3
# Copyright 2021 Clearpath Robotics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Roni Kreinin (rkreinin@clearpathrobotics.com)

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions.declare_launch_argument import DeclareLaunchArgument
from launch.conditions import LaunchConfigurationEquals
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node

def generate_launch_description():

    odom_relay = Node(
        package='topic_tools',
        executable='relay',
        name='turtlebot4_relay_odom',
        arguments=['/create3/odom', '/odom'],
        output='screen'
    )

    battery_relay = Node(
        package='topic_tools',
        executable='relay',
        name='turtlebot4_relay_battery',
        arguments=['/create3/battery_state', '/battery_state'],
        output='screen'
    )

    imu_relay = Node(
        package='topic_tools',
        executable='relay',
        name='turtlebot4_relay_imu',
        arguments=['/create3/imu', '/imu'],
        output='screen'
    )

    tf_relay = Node(
        package='topic_tools',
        executable='relay',
        name='turtlebot4_relay_tf',
        arguments=['/create3/tf', '/tf'],
        output='screen'
    )

    tf_static_relay = Node(
        package='topic_tools',
        executable='relay',
        name='turtlebot4_relay_tf_static',
        arguments=['/create3/tf_static', '/tf_static'],
        output='screen'
    )

    cmd_vel_relay = Node(
        package='topic_tools',
        executable='relay',
        name='turtlebot4_relay_cmd_vel',
        arguments=['/cmd_vel', '/create3/cmd_vel'],
        output='screen'
    )

    ld = LaunchDescription()
    ld.add_action(odom_relay)
    ld.add_action(battery_relay)
    ld.add_action(imu_relay)
    ld.add_action(tf_relay)
    ld.add_action(tf_static_relay)
    ld.add_action(cmd_vel_relay)
    return ld

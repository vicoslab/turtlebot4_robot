#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    tts_node = Node(
        package='piper_ros',
        executable='tts_node.py',
        name='tts_node',
        output='screen',
        emulate_tty=True
    )

    ld = LaunchDescription()
    ld.add_action(tts_node)
    return ld
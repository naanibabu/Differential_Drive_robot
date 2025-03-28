from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="teleop_twist_keyboard",
            executable="teleop_twist_keyboard",
            output="screen",
            prefix="xterm -e",  # Opens in a separate terminal window
            remappings=[("/cmd_vel", "/bumperbot_controller/cmd_vel_unstamped")]
        )
    ])

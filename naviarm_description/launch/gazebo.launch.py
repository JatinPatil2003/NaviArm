import os
from ament_index_python.packages import get_package_share_directory, get_package_prefix

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    SetEnvironmentVariable,
    TimerAction
)
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    naviarm_description_dir = get_package_share_directory("naviarm_description")
    naviarm_description_share = os.path.join(
        get_package_prefix("naviarm_description"), "share"
    )
    gazebo_ros_dir = get_package_share_directory("gazebo_ros")

    env_var = SetEnvironmentVariable("GAZEBO_MODEL_PATH", naviarm_description_share)

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("naviarm_description"),
                    "urdf",
                    "naviarm.xacro",
                ]
            ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[robot_description],
    )

    start_gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_dir, "launch", "gzserver.launch.py")
        ),
        launch_arguments={"verbose": "true"}.items()
    )

    start_gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_dir, "launch", "gzclient.launch.py")
        )
    )

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity",
            "naviarm",
            "-topic",
            "robot_description",
        ],
        output="screen",
    )

    delayed_spawner = TimerAction(period=10.0, actions=[spawn_robot])


    return LaunchDescription(
        [
            env_var,
            start_gazebo_server,
            start_gazebo_client,
            robot_state_publisher_node,
            delayed_spawner,
        ]
    )
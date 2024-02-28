import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

# This is the function launch system will look for
def generate_launch_description():
    # DATA INPUT
    urdf_file = 'box_bot_meshes_collisions_inertias.urdf'
    # xacro_file = "box_bot.xacro"
    package_description = "my_box_bot_gazebo"

    print("Fetching URDF ==>")
   # launch_file_path = os.path.join(get_package_share_directory(package_description), "launch", urdf_file)
    #robot_desc_path = os.path.join("home/sara/Desktop/dev_ws/src/my_box_bot_gazebo/models", 'box_bot_meshes_collisions_inertias.urdf' )
    robot_desc_path = os.path.join(get_package_share_directory(package_description), "models", 'box_bot_meshes_collisions_inertias.urdf')

    # Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        emulate_tty=True,
        #parameters=[{'use_sim_time': True, 'robot_description': Command(['xacro', robot_desc_path])}],
        parameters=[{'use_sim_time': True, 'robot_description': open(robot_desc_path, 'r' ).read()}],
        output="screen"
    )

    # RVIZ Configuration
    rviz_config_dir = os.path.join(get_package_share_directory(package_description), 'src/basic_mobile_robot/rviz', 'urdf_config.rviz')
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        name='rviz_node',
        parameters=[{'use_sim_time': True}],
        arguments=['-d', rviz_config_dir]
    )

    # Create and return launch description object
    return LaunchDescription([robot_state_publisher_node, rviz_node])



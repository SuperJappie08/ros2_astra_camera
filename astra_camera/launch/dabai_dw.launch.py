from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python import get_package_share_directory
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
import yaml


def generate_launch_description():
    params_file = get_package_share_directory("astra_camera") + "/params/dabai_dw_params.yaml"
    with open(params_file, 'r') as file:
        config_params = yaml.safe_load(file)
    container = ComposableNodeContainer(
        name='astra_camera_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='astra_camera',
                plugin='astra_camera::OBCameraNodeFactory',
                name='camera',
                namespace='camera',
                parameters=[config_params]
            ),
            ComposableNode(
                package='astra_camera',
                plugin='astra_camera::PointCloudXyzNode',
                namespace='camera',
                name='point_cloud_xyz')
        output='screen'
    )
    rviz_config_dir = get_package_share_directory(
        "astra_camera") + '/rviz/pointcloud.rviz'
    rviz_node = Node(package='rviz2',
                     executable='rviz2',
                     name='rviz2',
                     output='screen',
                     arguments=['-d', rviz_config_dir],
                     parameters=[{
                         'use_sim_time': False
                     }])
    return LaunchDescription([container, rviz_node])

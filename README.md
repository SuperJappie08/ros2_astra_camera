```bash
echo "deb [trusted=yes] https://github.com/SuperJappie08/ros2_astra_camera/raw/ros_mirte_humble_jammy_arm64/ ./" | sudo tee /etc/apt/sources.list.d/SuperJappie08_ros2_astra_camera.list
echo "yaml https://github.com/SuperJappie08/ros2_astra_camera/raw/ros_mirte_humble_jammy_arm64/local.yaml humble" | sudo tee /etc/ros/rosdep/sources.list.d/1-SuperJappie08_ros2_astra_camera.list
```

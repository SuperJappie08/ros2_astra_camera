#pragma once

#if __has_include(<cv_bridge/cv_bridge.h>)
#define ROS2_HUMBLE
#else
#define ROS2_JAZZY
#endif
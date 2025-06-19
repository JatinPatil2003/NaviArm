# 🤖 NaviArm

**NaviArm** is a fully integrated mobile manipulation system combining an autonomous mobile robot (AMR) base with a 7-DOF xArm robotic arm. Built on **ROS 2 Humble**, it supports real-time navigation, motion planning, and Gazebo-based simulation for research, prototyping, and industrial applications.

---

## 🚀 Key Features

- 🌐 **Autonomous Navigation** using SLAM/AMCL + Nav2
- 🦾 **7-DOF xArm Manipulator** integrated with MoveIt 2
- 🧠 **Motion Planning** with RViz interface and execution
- 🧪 **Gazebo Simulation** with realistic world environments
- 🧩 Modular architecture with ROS 2 packages and submodules

---

## 📂 Repository Structure

```
NaviArm/
├── naviarm_description/         # Combined URDF/Xacro for full robot
├── naviarm_gazebo/              # Gazebo launch files and models
├── autoserve_description/       # AMR base description (submodule)
├── xarm_description/            # xArm 7 DOF robot (submodule)
├── xarm_moveit_config/          # MoveIt config package for xArm
├── autoserve_navigation/        # Nav2 SLAM/AMCL + map configs
└── ...
```

---

## ⚙️ Setup Instructions

### 1. Clone with Submodules
```bash
git clone --recurse-submodules https://github.com/<your-org>/NaviArm.git
cd NaviArm
```

### 2. Build the Workspace
```bash
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

### 3. Check Your Environment
Install these dependencies if not already:
```bash
sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui ros-humble-gazebo-ros-pkgs
sudo apt install ros-humble-nav2-bringup ros-humble-moveit ros-humble-controller-manager
```

---

## 🧪 Simulation in Gazebo

Launch full robot simulation with controllers and world:
```bash
ros2 launch naviarm_gazebo gazebo.launch.py
```

---

## 🗺️ AMR Navigation

Start SLAM or localization + Nav2 planner:
```bash
ros2 launch autoserve_navigation navigation.launch.py
```

---

## 🦾 Manipulation with MoveIt

Control and plan robot arm trajectories with MoveIt:
```bash
ros2 launch xarm_moveit_config xarm7_moveit_gazebo.launch.py
```

---

## 🛠 Controller Setup

Verify loaded controllers:
```bash
ros2 control list_controllers
ros2 control list_hardware_interfaces
```

---

## 🧰 Tools & Integrations

- ✅ \`ros2_control\` with hardware plugins
- ✅ Gazebo + RViz visualizations
- ✅ TF broadcasting & joint states
- ✅ Modular hardware abstraction for real robot usage (optional)

---

## 📌 Future Improvements

- [ ] Add gripper and object manipulation demo
- [ ] Integrate perception (Intel RealSense)
- [ ] Docking and battery monitoring
- [ ] Fleet management

---

## 🧑‍💻 Maintainer

Developed by [@JatinPatil2003](https://github.com/JatinPatil2003)

---

## 🛡️ License

This project is licensed under [MIT License](LICENSE)

---

## 🆘 Issues & Contributions

Found a bug or have an idea?  
Open an issue or PR: [github.com/<your-org>/NaviArm/issues](https://github.com/<your-org>/NaviArm/issues)

---
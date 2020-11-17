
## To install the jackal image on the hard drive:

1. Download the latest iso from Clearpath at:
http://packages.clearpathrobotics.com/stable/images/latest/

2. Put this image on thumb drive using a tool such as Unetbootin
    - See: https://unetbootin.github.io/
    - Or install Unetbooton on Ubuntu with:<br>
`sudo apt-get install unetbootin`

3. Connect the USB thumbdrive to the Jackal computer and boot to it. You can get to the boot options by pressing <kbd>del</kbd> while booting up.

4. After the USB thumbdrive install is complete, turn off the computer and remove the USB device.

5. Restart the computer and you will be prompted to enter a computer name, by convention we are calling them jackal## (ie jackal01).

6. Modify the network settings:
    - Edit /etc/network/interface to match the interface file in this repo

7. Enable the computer to automatically connect to the desired wifi access points:
    - In a terminal run: `wicd-curses`
    - The documentation for this application is found at: http://wicd.sourceforge.net/
    - The ip address should be a known static address

8. Modify the .bashrc file (this repo contains an example of a modified bashrc file):
    - Source the local ros workspace
    - Modify ROS_IP and ROS_MASTER_URI to use the static wifi IP address. (http://wiki.ros.org/ROS/Tutorials/MultipleMachines)

9. Add global git settings
    - `git config --global user.email "administrator@jackal01.com"`
    - `git config --global user.name "Administrator Jackal"`
    - `git config --global push.default simple`

10. Create a local ros workspace in the users home directory.
    - `mkdir -p ~/catkin_ws/src`
    - `cd ~/catkin_ws/`
    - `catkin_make`
    
11. Install the usma_jackal ros package.
    - `cd ~/catkin_ws/src`
    - `git clone https://github.com/westpoint-robotics/usma_jackal.git`

12. Enable a ros robot-upstart service to automatically start the required ros nodes.
    - `rosrun robot_upstart install usma_jackal/launch/bringup.launch`

#### To access the ros topics on a remote computer you should install the ros jackal packages.
- `sudo apt-get install ros-kinetic-jackal*`

## To Incorporate SARA Modular Sensor Unit int Jackal URDF:

0. If you have a version of usma_jackal predating 17 Nov, 2020, download the sara_description package from this repository, and place it in usma_jackal.
1. On your local machine, navigate to usma_jackal/urdf.
2. Open "jackal.urdf.xacro".
3. Just above the close robot tag (`</robot>`) insert an include for the SARA URDF.
    - `<xacro:include filename="$(find sara_description)/urdf/sara_seventeen.urdf.xacro"/>`
4. Save the Jackal URDF.
5. In a terminal, you can now run RViz, and or Gazebo and view/use the robot with the SARA sensor unit installed.
    - `roslaunch jackal_gazebo jackal_world.launch` followed by
    - `roslaunch jackal_viz view_robot.launch`
    OR, you can run RViz alone with:
    - `roslaunch jackal_viz view_model.launch`

##### TODO: 
    - Move joystick node to its own launch file
    - Add URDF for VLP16 to robot
    - Tune joystick params for smoother control
    - Enable indoor mapping and navigation



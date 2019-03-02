
## To install the jackal image on the hard drive:

1. Download the latest iso from Clearpath at:
http://packages.clearpathrobotics.com/stable/images/latest/

2. Put this image on thumb drive using a tool such as Unetbootin
- See: https://unetbootin.github.io/
- Or install on Ubuntu with:<br>
`sudo apt-get install unetbootin`

3. Connect the USB thumbdrive to the Jackal computer and boot to it. You can get to the boot options by pressing <del> while booting up.

4. After the USB thumbdrive install is complete, turn off the computer and remove the USB device.

5. Restart the computer and you will be prompted to enter a computer name, by convention we are calling them jackal## (ie jackal01).

6. Modify the network settings:
- Edit /etc/network/interface to match the interface file in this repo

7. Enable the computer to automatically connect to the desired wifi access points:
- In a terminal run: `wicd-curses`
- The documentation for this application is found at: https://wiki.archlinux.org/index.php/wicd
- The ip address should be a known static address

8. Create a local ros workspace in the users home directory.

9. Modify the .bashrc file (this repo contains an example of a modified bashrc file):
- Source the local ros workspace
- Modify ROS_IP and ROS_MASTER_URI to use the static wifi IP address.

10. Add global git settings
-`git config --global user.email "administrator@jackal01.com"`
-`git config --global user.name "Administrator Jackal"`

11. Install the usma_jackal ros package.
- `cd ~/catkin_ws/src`
- `git clone https://github.com/westpoint-robotics/usma_jackal.git`

12. Enable a ros robot-upstart service to automatically start the required ros nodes.
- rosrun robot_upstart install usma_jackal/launch/bringup.launch

#### To access the ros topics on a remote computer you should install the ros jackal packages.
- `sudo apt-get install ros-kinetic-jackal-*`





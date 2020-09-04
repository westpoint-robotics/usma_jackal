import rospy

from sensor_msgs import Joy
from geometry_msgs import Twist

class Jackal:
    '''
    JackalJ class contains all variables and methods necessary to deal
    with the PS4 joystick inputs and motor velocity outputs.
    '''
    def __init__(self):
        self.joy_dpad_up    = 0 #D pad up arrow
        self.joy_dpad_down  = 0 #D pad down arrow
        self.joy_dpad_left  = 0 #D pad left arrow
        self.joy_dpad_right = 0 #D pad right arrow
        self.joy_trigger_l1 = 0 #D pad L1 trigger
        self.joy_triangle   = 0 #D pad triangle button
        
        self.vel_linear_x   = 0 #Drive forward (+), and backward (-)
        self.vel_linear_y   = 0
        self.vel_linear_z   = 0
        self.vel_angular_x  = 0
        self.vel_angular_y  = 0
        self.vel_angular_z  = 0 #Turn left (+), and right (-)
        
        rospy.Subscriber("/bluetooth_teleop/joy", Joy, self.joy_callback)
        rospy.Publisher("/bluetooth_teleop/cmd_vel", Twist, self.drive)
        
        def joy_callback(self, msg):
            self.joy_dpad_up    = msg.buttons[13]
            self.joy_dpad_down  = msg.buttons[14]
            self.joy_dpad_left  = msg.buttons[11]
            self.joy_dpad_right = msg.buttons[12]
            self.joy_trigger_l1 = msg.buttons[4]
            self.joy_triangle   = msg.buttons[3]
        
        def drive(self):
            vel_linear_multiplier = 0
            vel_angular_multiplier = 0
            pub = rospy.Publisher('chatter', Twist, queue_size=10)
            rospy.init_node('drive', anonymous=True)
            rate = rospy.Rate(10) # 10hz
            while not rospy.is_shutdown():
                #if L1 == 1:
                #   vel_linear_multiplier = 0.4
                #   vel_angular_multiplier = 0.4
                #if Triangle == 1:
                #   vel_linear_multiplier = 2
                #   vel_angular_multiplier = 2
                #if D pad up == 1:
                #   vel_linear_x = vel_linear_multiplier
                #if D pad down == 1:
                #   vel_linear_x = vel_linear_multiplier * -1
                #if D pad left == 1:
                #   vel_angular_x = vel_angular_multiplier
                #if D pad right == 1:
                #   vel_angular_x = vel_angular_multiplier * -1
                if(self.joy_trigger_l1 == 1):
                    vel_linear_multiplier = 0.4
                    vel_angular_multiplier = 0.4
                if(self.joy_triangle == 1):
                    vel_linear_multiplier = 2
                    vel_angular_multiplier = 2
                if(self.joy_dpad_up == 1):
                    self.vel_linear_x = vel_linear_multiplier
                if(self.joy_dpad_down == 1):
                    self.vel_linear_x = vel_linear_multiplier * -1
                if(self.joy_dpad_left == 1):
                    self.vel_angular_x = vel_angular_multiplier
                if(self.joy_dpad_right == 1):
                    self.vel_angular_x = vel_angular_multiplier * -1
                twist = Twist()
                twist.linear.x  = self.vel_linear_x 
                twist.angular.z = self.vel_angular_z
                rospy.loginfo(twist)
                pub.publish(twist)
                rate.sleep()
                
if __name__ == "__main__":
    
    demo_jackal = Jackal()

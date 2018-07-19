#define _USE_MATH_DEFINES

#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <stdlib.h>
#include <cmath>

int main(int argc, char **argv) {

  ros::init(argc, argv, "figure_eight_commands");
  ros::NodeHandle nh;

  ros::Publisher pub=nh.advertise<geometry_msgs::Twist>("cmd_vel", 100);

  ros::Rate rate(200);

  double linear_v = .25;
  double angular_v = .35;
  double period = 2.2*M_PI/angular_v;
  double t_0 = ros::Time::now().toSec();

  while(ros::ok()) {

        geometry_msgs::Twist msg;

            msg.linear.x=linear_v;
                if(fmod(ros::Time::now().toSec()-t_0,2*period)-period < 0){
                          msg.angular.z=angular_v;
                              }
                    else {
                              msg.angular.z=-1*angular_v;
                                  }

                        pub.publish(msg);

                            rate.sleep();
                                }
}   

cmake_minimum_required(VERSION 2.8.3)
project(contact_charger)

find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	message_generation
	std_msgs
)

add_service_files(
	FILES
)

catkin_python_setup()

generate_messages(DEPENDENCIES std_msgs)

catkin_package(
	CATKIN_DEPENDS std_msgs message_runtime 
)

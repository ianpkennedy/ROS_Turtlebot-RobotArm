### Homework 2

Ian Kennedy

## Part 1

Part 1 of the homework creates a figure eight motion in a variety of platforms. THe trajectory node publishes the figure eight trajectory, while the simodom node handles simulation specific platform conversions for turtlesim and Rviz. It also subscribes to the turtlesim pose and publishes an odometry message. The figure_eight.launch file  launches the nodes for simulation (mode:=sim) or for the turtlebot (sim:=real)

The calculations performed for part 1 are detailed in Calculations.jpg (source: http://ipco-co.com/PET_Journal/presented%20papers/Poster/002.pdf , accessed 10/08. source: http://www.alcyone.com/max/reference/maths/trigonometry.html, accessed 10/08)

In order to launch the simulation, perform the following roslaunch command 
`roslaunch homework2 figure_eight.launch mode:=sim`

In order to run the figure eight on a turtlebot, perform the appropriate setup instructions at the following link: https://nu-msr.github.io/me495_site/turtlebot3/turtlebot3.html

Then, run the following command in ROS:
`roslaunch homework2 figure_eight.launch mode:=real`

Videos can be found here:
- Rviz: https://drive.google.com/file/d/15QMGKcQZelHSi6WOPE75VDkCTaUyIsSn/view?usp=sharing
- turtlesim: https://drive.google.com/file/d/1e04FHbHZuz6ry3XCZVjnIkW92Xe_NwFZ/view?usp=sharing 
- On a real turtlebot: https://drive.google.com/file/d/1WBGLXYgAfla4xsxKw3uB7OaM3i0Lm2Pv/view?usp=sharing


## Part 2

For part 2 of the homework, we created a two link arm to and creates a trajectory for it to follow. arm_traj is the node that creates the trajectory for the two link arm joint states, and can drive the two link arm in rviz. arm_marker creates markers at the appropriate points of the end effector at fixed intervals.

In order to run show the arm in rviz and command it with a joint state publisher gui, perform the following command:
`roslaunch homework2 arm_mark.launch use_jsp:=true`

In order to show the two link arm following the trajectory, perform the following roslaunch command to view the two link arm following a trajectory, using arm_mark.launch:
`roslaunch homework2 arm_mark.launch use_jsp:=false`

This command will launch the joint_state_publisher_gui:
`roslaunch homework2 arm_mark.launch use_jsp:=false`


arm_basics.launch simply launches the arm in rviz:
`roslaunch homework2 arm_basics.launch use_jsp:=false`

Alternatively, arm_basics.launch can be used to control the arm with the joint_state_publisher_gui with the following:

`roslaunch homework2 arm_basics.launch use_jsp:=true`


When following the trajectory, a green sphere is published in the +x area, and a yellow cube in the -x area (at the point of the end effector).


## Sources/Misc.
For the URDF construction: http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch (accessed 10/16)

http://wiki.ros.org/xacro#Macros (accessed 10/16)


For launch file development:
http://wiki.ros.org/roslaunch/XML/arg (10/17)

https://answers.ros.org/question/213075/publish-joint_state-with-python-to-rviz/ (accessed 10/17)

http://wiki.ros.org/roslaunch/XML (accessed 10/17)

https://answers.ros.org/question/12756/roslaunch-if-condition/ (10/17)

https://campus-rover.gitbook.io/lab-notebook/faq/using-conditionals-in-roslaunch (accessed 10/17)

https://answers.ros.org/question/51525/roslaunch-xml-boolean-operators/ (10/18)

All turtlebot3 packages cloned and reviewed on 10/14 from this link: https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

Collaborated briefly with:
Matthew Short

Bhagyesh Agresar


robot_location = 30
ball_location = 35
goal_location = 20
have_ball = False

# this if statment will print the text if the ball's location is greater than the robot's location 
if robot_location < ball_location:
    print("Almost at the ball")

# this if statment will print the text if the robots's location is greater than the goal's location 
if robot_location > goal_location:
    print("You are beyond the goal.")

# this if statment will print the text if the robot and goal location is the same
if robot_location == goal_location:
    print("The robot is at the goal.")

robot_location += 5

# # this if statment will print the text if the robot and goal location is the same
if robot_location == goal_location:
    print("At the goal.")

# this if statment will print if the robot and the ball are at the same location 
if robot_location == ball_location:
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 15

# this if statment will print the following text if the goal_location is farther than the robot_location 
if robot_location < goal_location:
    print("You went too far.")

# this if statment
if robot_location == goal_location and have_ball is True:
    print("You scored a goal!")
    have_ball = False
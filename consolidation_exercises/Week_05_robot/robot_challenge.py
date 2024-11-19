#from cpa_robot import position_x, position_y, orientation, drive, plot_path, reset_robot, plot_robot, sensor_left, sensor_middle, sensor_right
#reset_robot()

#import random
#import math

#goto_num = int(input("How many zones would you like to search? "))

#goto_x = int(input("Search x: "))
#goto_y = int(input("Search y: "))

#drive to inputed points and search 5 cm radius of point 

#def randSearch():
#    for j in range(0,100):
#        search_angle = 2*math.pi*random.random()
#        drive(2.5*search_angle,-2.5*search_angle)
#        while ((position_x() - (goto_x))**2 + (position_y() - (goto_y))**2)**0.5 < 5:
#            drive(0.1,0.1)
#            break

#def goto():
#    round(position_x(), 5) 
#    round(position_y(), 5) 
#    a = (goto_x - position_x())
#    b = (goto_y - position_y())
#    print("a and b: " , a,b)
#    angle = math.atan((a) / (b))
#    error = angle - orientation()
#    dist = ((2.5*error))
#    length = (((goto_x - position_x())**2) + ((goto_y - position_y())**2))**(0.5)
#    if goto_y > position_y() and goto_x > position_x():
#        drive(dist,-dist)
#    elif goto_y < position_y() and goto_x > position_x():
#        drive(-dist-(3.75*math.pi),dist+(3.75*math.pi))
#    elif goto_y < position_y() and goto_x < position_x():
#        drive(dist + (2.5*math.pi),-dist - (2.5*math.pi))
#    elif goto_y > position_y() and goto_x < position_x():
#        drive(dist + (5*math.pi), -dist - (5*math.pi))
#    drive(length,length)
#    print("need to be at", goto_x,",", goto_y, "at", position_x(), position_y())
#    round(position_x(),5)
#    round(position_y(),5)
#    print("a and b:" , a , b)
#    randSearch()

#for i in range(0,goto_num):
#    goto()

#while sensor_middle() == True:
#    print("sensor activated")


#plot_path()

import random
from math import sqrt, atan2, pi

# Define a function for user interaction and robot path search
def search_points_with_collision():
    # Ask the user for the number of points to search
    num_points = int(input("Enter the number of points to search: "))

    # Initialize the robot at the origin
    reset_robot()

    # Define movement parameters
    search_radius = 5.0  # Radius around each point to search within
    collision_distance = -2.0  # Distance to reverse when a collision is detected

    for _ in range(num_points):
        # Generate a random target within a 5-unit radius
        random_angle = random.uniform(0, 2 * pi)
        distance = random.uniform(0, search_radius)
        target_x = position_x() + distance * cos(random_angle)
        target_y = position_y() + distance * sin(random_angle)

        print(f"Searching around target point at ({target_x:.2f}, {target_y:.2f})")

        # Move the robot to the target while avoiding obstacles
        while True:
            angle_to_target = atan2(target_y - position_y(), target_x - position_x())
            drive_distance = 1.0  # Set a small movement step size

            # Calculate the drive parameters for moving toward the target
            drive_left = drive_distance + angle_to_target * 0.5  # Add a slight turn based on angle
            drive_right = drive_distance - angle_to_target * 0.5

            # Move the robot in small steps towards the target
            drive(drive_left, drive_right)

            # Check if any sensors are triggered (indicating a collision)
            if sensor_left() or sensor_middle() or sensor_right():
                print("Collision detected! Bouncing back.")
                # Reverse the robot to simulate a bounce back
                drive(collision_distance, collision_distance)

                # Choose a new random target in the vicinity after collision
                random_angle = random.uniform(0, 2 * pi)
                distance = random.uniform(0, search_radius)
                target_x = position_x() + distance * cos(random_angle)
                target_y = position_y() + distance * sin(random_angle)
                print(f"New target after collision: ({target_x:.2f}, {target_y:.2f})")
                continue

            # Break loop if within a close range to the target point
            if sqrt((target_x - position_x())**2 + (target_y - position_y())**2) < 0.5:
                print(f"Reached target point ({target_x:.2f}, {target_y:.2f})")
                break

    # Display the search path after completing all points
    plot_path()

# Run the search function if the script is executed directly
if __name__ == '__main__':
    search_points_with_collision()

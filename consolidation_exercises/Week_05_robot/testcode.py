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

from random import choice

class RandomWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=50000):
        """Initialize the attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4, 5,6,7,8])
            y_step = y_direction * y_distance

    
    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until walk reaches desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far
            
            x_step = get_step()

            
            y_step = get_step()

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)    

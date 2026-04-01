# world_mantle.py
# Earth's mantle layer

class Mantle:
    def __init__(self, inner_radius=20, outer_radius=35):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.material = "silicate rock"
        self.temperature = "1000-3700°C"
        self.properties = {
            "density": "3.3-5.7 g/cm³",
            "composition": "silicon, oxygen, magnesium, iron, aluminum",
            "state": "solid (plastic flow)",
            "pressure": "1.3-135 GPa",
            "thickness": "2900 km"
        }

    def get_points(self, grid):
        """Get points in mantle layer (between inner and outer radius)"""
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if self.inner_radius*self.inner_radius < distance_squared <= self.outer_radius*self.outer_radius:
                points.append(point)
        return points

    def get_upper_mantle_points(self, grid):
        """Upper mantle: transition zone"""
        upper_inner = self.inner_radius
        upper_outer = int((self.inner_radius + self.outer_radius) * 0.7)  # ~70% of mantle
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if upper_inner*upper_inner < distance_squared <= upper_outer*upper_outer:
                points.append(point)
        return points

    def get_lower_mantle_points(self, grid):
        """Lower mantle: deeper part"""
        lower_inner = int((self.inner_radius + self.outer_radius) * 0.7)
        lower_outer = self.outer_radius
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if lower_inner*lower_inner < distance_squared <= lower_outer*lower_outer:
                points.append(point)
        return points
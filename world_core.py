# world_core.py
# Earth's core layers: Inner Core and Outer Core

class InnerCore:
    def __init__(self, radius=10):
        self.radius = radius
        self.material = "solid iron-nickel alloy"
        self.temperature = "5000-6000°C"
        self.properties = {
            "density": "12.8-13.1 g/cm³",
            "composition": "iron (80-85%), nickel (5-10%), lighter elements",
            "state": "solid",
            "pressure": "330-360 GPa",
            "temperature": self.temperature
        }

    def get_points(self, grid):
        """Get points within inner core radius"""
        points = []
        for point in grid.points:
            x, y, z = point
            if x*x + y*y + z*z <= self.radius * self.radius:
                points.append(point)
        return points

class OuterCore:
    def __init__(self, inner_radius=10, outer_radius=20):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.material = "liquid iron-nickel alloy"
        self.temperature = "4000-5000°C"
        self.properties = {
            "density": "9.9-12.2 g/cm³",
            "composition": "iron (80-90%), nickel, sulfur, oxygen",
            "state": "liquid",
            "pressure": "135-330 GPa",
            "temperature": self.temperature
        }

    def get_points(self, grid):
        """Get points in outer core (between inner and outer radius)"""
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if self.inner_radius*self.inner_radius < distance_squared <= self.outer_radius*self.outer_radius:
                points.append(point)
        return points
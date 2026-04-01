# world_crust.py
# Earth's crust layer

class Crust:
    def __init__(self, inner_radius=35, outer_radius=40):
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.material = "igneous, sedimentary, and metamorphic rocks"
        self.temperature = "0-400°C (surface to bottom)"
        self.properties = {
            "density": "2.2-2.9 g/cm³ (continental), 2.9-3.0 g/cm³ (oceanic)",
            "composition": "silicon, oxygen, aluminum, iron, calcium",
            "state": "solid",
            "pressure": "0-1.3 GPa",
            "thickness": "5-70 km",
            "temperature": self.temperature
        }

    def get_points(self, grid):
        """Get points in crust layer (between inner and outer radius)"""
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if self.inner_radius*self.inner_radius < distance_squared <= self.outer_radius*self.outer_radius:
                points.append(point)
        return points

    def get_continental_crust_points(self, grid):
        """Continental crust points (thicker, less dense)"""
        # For simplicity, we'll consider the outermost part as continental
        continental_inner = int((self.inner_radius + self.outer_radius) * 0.8)
        continental_outer = self.outer_radius
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if continental_inner*continental_inner < distance_squared <= continental_outer*continental_outer:
                points.append(point)
        return points

    def get_oceanic_crust_points(self, grid):
        """Oceanic crust points (thinner, denser)"""
        oceanic_inner = self.inner_radius
        oceanic_outer = int((self.inner_radius + self.outer_radius) * 0.8)
        points = []
        for point in grid.points:
            x, y, z = point
            distance_squared = x*x + y*y + z*z
            if oceanic_inner*oceanic_inner < distance_squared <= oceanic_outer*oceanic_outer:
                points.append(point)
        return points
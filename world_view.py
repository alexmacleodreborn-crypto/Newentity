# world_view.py
# Complete Earth world view combining grid and layers

from world_grid import WorldGrid
from world_core import InnerCore, OuterCore
from world_mantle import Mantle
from world_crust import Crust

class WorldView:
    def __init__(self, radius=50):
        self.grid = WorldGrid(radius)
        self.grid.generate()

        # Initialize Earth layers with proportional radii
        total_radius = radius
        self.inner_core = InnerCore(radius=int(total_radius * 0.1))  # ~10% of radius
        self.outer_core = OuterCore(
            inner_radius=int(total_radius * 0.1),
            outer_radius=int(total_radius * 0.4)
        )
        self.mantle = Mantle(
            inner_radius=int(total_radius * 0.4),
            outer_radius=int(total_radius * 0.9)
        )
        self.crust = Crust(
            inner_radius=int(total_radius * 0.9),
            outer_radius=total_radius
        )

    def get_layer_info(self):
        """Get information about all layers"""
        return {
            "Inner Core": {
                "points": len(self.inner_core.get_points(self.grid)),
                "properties": self.inner_core.properties
            },
            "Outer Core": {
                "points": len(self.outer_core.get_points(self.grid)),
                "properties": self.outer_core.properties
            },
            "Mantle": {
                "points": len(self.mantle.get_points(self.grid)),
                "properties": self.mantle.properties
            },
            "Crust": {
                "points": len(self.crust.get_points(self.grid)),
                "properties": self.crust.properties
            }
        }

    def get_all_points_by_layer(self):
        """Get all points organized by layer"""
        return {
            "inner_core": self.inner_core.get_points(self.grid),
            "outer_core": self.outer_core.get_points(self.grid),
            "mantle": self.mantle.get_points(self.grid),
            "crust": self.crust.get_points(self.grid)
        }

    def get_total_points(self):
        """Get total points in the world"""
        return len(self.grid.points)

if __name__ == "__main__":
    world = WorldView(radius=40)

    print("Earth World View Generated")
    print(f"Total grid points: {world.get_total_points()}")

    layer_info = world.get_layer_info()
    for layer_name, info in layer_info.items():
        print(f"\n{layer_name}:")
        print(f"  Points: {info['points']}")
        print(f"  Density: {info['properties']['density']}")
        print(f"  Temperature: {info['properties'].get('temperature', 'N/A')}")

    # Example: Get points for visualization
    points_by_layer = world.get_all_points_by_layer()
    print(f"\nInner core sample points: {points_by_layer['inner_core'][:5]}")
    print(f"Crust sample points: {points_by_layer['crust'][:5]}")
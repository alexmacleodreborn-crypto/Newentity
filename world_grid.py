# world_grid.py
# A7DO Core: Pure spherical grid (voxel lattice)

import math

class WorldGrid:
    def __init__(self, radius=50):
        self.radius = radius
        self.points = set()

    def generate(self):
        r = self.radius

        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                for z in range(-r, r + 1):

                    # Sphere equation: x^2 + y^2 + z^2 <= r^2
                    if x*x + y*y + z*z <= r*r:
                        self.points.add((x, y, z))

        print(f"Generated {len(self.points)} points inside sphere")

    def is_inside(self, x, y, z):
        return (x*x + y*y + z*z) <= self.radius * self.radius


if __name__ == "__main__":
    grid = WorldGrid(radius=20)
    grid.generate()

    # Example: print first 10 points
    print(list(grid.points)[:10])

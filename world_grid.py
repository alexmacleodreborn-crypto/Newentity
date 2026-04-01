# world_grid.py
# A7DO: 3D rotating voxel sphere viewer

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


class WorldGrid:
    def __init__(self, radius=20):
        self.radius = radius
        self.points = []

    def generate(self):
        r = self.radius

        for x in range(-r, r + 1):
            for y in range(-r, r + 1):
                for z in range(-r, r + 1):
                    if x*x + y*y + z*z <= r*r:
                        self.points.append((x, y, z))

        print(f"Generated {len(self.points)} points")


# ===== VISUALISER =====

class Viewer:
    def __init__(self, points):
        self.points = np.array(points)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Extract coords
        self.x = self.points[:, 0]
        self.y = self.points[:, 1]
        self.z = self.points[:, 2]

        # Plot
        self.scatter = self.ax.scatter(self.x, self.y, self.z, s=2)

        self.ax.set_box_aspect([1,1,1])
        self.ax.set_xlim(-25, 25)
        self.ax.set_ylim(-25, 25)
        self.ax.set_zlim(-25, 25)

        self.angle = 0

    def update(self, frame):
        self.angle += 1
        self.ax.view_init(elev=20, azim=self.angle)
        return self.scatter,

    def run(self):
        anim = FuncAnimation(self.fig, self.update, frames=360, interval=30)
        plt.show()


# ===== RUN =====

if __name__ == "__main__":
    grid = WorldGrid(radius=20)
    grid.generate()

    viewer = Viewer(grid.points)
    viewer.run()

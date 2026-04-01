# Earth World Grid System

This project creates a 3D spherical grid representing Earth's internal structure with separate layers for core, mantle, and crust components.

## Files

- `world_grid.py` - Core spherical grid generation using voxel lattice
- `world_core.py` - Inner and outer core layers with physical properties
- `world_mantle.py` - Mantle layer with upper/lower mantle subdivisions
- `world_crust.py` - Crust layer with continental/oceanic crust types
- `world_view.py` - Main integration file that combines all layers

## Usage

Run the complete Earth model:

```bash
python world_view.py
```

This will generate a spherical grid and display information about each Earth layer including:
- Number of grid points in each layer
- Physical properties (density, temperature, composition, etc.)
- Sample coordinate points for visualization

## Layer Structure

The Earth is modeled with proportional radii:
- **Inner Core**: 0-10% of radius (solid iron-nickel)
- **Outer Core**: 10-40% of radius (liquid iron-nickel)
- **Mantle**: 40-90% of radius (silicate rock)
- **Crust**: 90-100% of radius (igneous/sedimentary rocks)

## Classes

Each layer file contains classes with methods to:
- `get_points(grid)` - Return all points within that layer
- Access physical properties and material information

The `WorldView` class in `world_view.py` integrates everything and provides methods to analyze the complete Earth model.
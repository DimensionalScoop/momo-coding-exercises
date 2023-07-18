from vents import *

for i in range(10):
    start_points, end_points = load_vent_lines("input")
    ocean = draw_ocean_floor(start_points, end_points)
    n_crossings = count_vent_crossings(ocean)
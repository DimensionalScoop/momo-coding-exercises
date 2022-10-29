import vents

def test_vent_crossings():
    start_points, end_points = vents.load_vent_lines("adventofcode21/max_d5/test_input")
    ocean = vents.draw_ocean_floor(start_points, end_points)
    n_crossings = vents.count_vent_crossings(ocean)
    assert n_crossings == 12
import sys
import solutils

def solution(json_input):
    """Processes train and test grids"""

    for i in ['train', 'test']:
        for j in range(0, len(json_input.get(i))):
            grid = json_input.get(i)[j]['input']
            sol = solve(grid)
            solutils.print_grid(sol)
            print('', end='\n')


def solve(grid):
    """Solves task 11852cab

    This task gets all coloured positions, extracts different parts and then
    evaluates which colours to use for different parts (corners, middel ring,
    sides, centre). The final bit is to colour uncoloured spots on the grid
    and return it.
    """

    # Get main shape
    results = solutils.get_all_coloured(grid)
    # Get centre point and parts
    centre = solutils.find_centre(results)
    corners, sides, middle = solutils.parts_11852cab(centre)
    # Get part colours
    corner_colour = solutils.part_colours_11852cab(corners, grid)
    side_colour = solutils.part_colours_11852cab(sides, grid)
    middle_colour = solutils.part_colours_11852cab(middle, grid)
    centre_colour = solutils.part_colours_11852cab([centre], grid)
    if not corner_colour and centre_colour: # if no corners, use centre_colour
        corner_colour = centre_colour
    if not middle_colour and centre_colour:
        middle_colour = centre_colour
    if not side_colour and centre_colour:
        side_colour = centre_colour
    # Ensure all positions on the shape are coloured
    solutils.paint_positions(corners, corner_colour, grid)
    solutils.paint_positions(middle, middle_colour, grid)
    solutils.paint_positions(sides, side_colour, grid)
    return grid


def main(json_file):
    json_input = solutils.load_task(json_file)
    solution(json_input)


if __name__ == '__main__':
    main(sys.argv[1])

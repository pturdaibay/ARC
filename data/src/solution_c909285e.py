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
    """Solves task c909285e

    This task extracts all available shapes where shapes are formed by positions
    connecting on their sides with the same colour.
    Once all shapes are extracted, the unique colour shape is found, and the
    positions the shape encloses are extracted from the grid.
    """

    results = solutils.shapes(grid, btype='side', colour=True)
    # Find the square in all shapes, should be a different colour
    colour_count = dict()
    square = solutils.find_unique_c909285e(results, grid)
    minx, maxx, miny, maxy = solutils.find_min_max(results[square[0]])
    output_grid = []
    for y in range(miny, maxy + 1):
        output_grid.append(grid[y][minx: maxx + 1])
    return output_grid


def main(json_file):
    json_input = solutils.load_task(json_file)
    solution(json_input)


if __name__ == '__main__':
    main(sys.argv[1])

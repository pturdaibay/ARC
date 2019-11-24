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
    """Solves task 67385a82

    This task finds shapes using positions connected on their sides and having
    the same colour.
    Once all shapes are extracted, those that are formed by more than one
    position are coloured blue (8).
    """

    results = solutils.shapes(grid, btype='side', colour=True)
    for shape in results:
        if len(shape) > 1: #shape to colour
            solutils.paint_positions(shape, 8, grid)
    return grid


def main(json_file):
    json_input = solutils.load_task(json_file)
    solution(json_input)


if __name__ == '__main__':
    main(sys.argv[1])

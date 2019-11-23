import sys
import json
import shapes


def solve(grid):
    """Solves task 67385a82"""

    def paint_blue(shape, grid):
        """Paints shapes blue on the grid
        shape: list of positions to paint
        grid: colour values for each position"""
        for x,y in shape:
            grid[y][x] = 8

    results = shapes.shapes(grid, btype='side', colour=True)
    for shape in results:
        if len(shape) > 1: #shape to colour
            paint_blue(shape, grid)
    return grid

def main(json_file):
    try:
        with open(json_file, 'r') as jinput:
            raw_input = json.load(jinput)
    except FileNotFoundError as e:
        print(f'Error, file not found: {json_file}')
        return

    for i in ['train', 'test']:
        for j in range(0, len(raw_input.get(i))):
            grid = raw_input.get(i)[j]['input']
            sol = solve(grid)
            shapes.print_grid(sol)
            print('', end='\n')



if __name__ == '__main__':
    main(sys.argv[1])

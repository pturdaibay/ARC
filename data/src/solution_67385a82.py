import sys
import solutils

def solution(json_input):
    for i in ['train', 'test']:
        for j in range(0, len(json_input.get(i))):
            grid = json_input.get(i)[j]['input']
            sol = solve(grid)
            solutils.print_grid(sol)
            print('', end='\n')


def solve(grid):
    """Solves task 67385a82"""

    def paint_blue(shape, grid):
        """Paints shapes blue on the grid
        shape: list of positions to paint
        grid: colour values for each position"""
        for x,y in shape:
            grid[y][x] = 8

    results = solutils.shapes(grid, btype='side', colour=True)
    for shape in results:
        if len(shape) > 1: #shape to colour
            paint_blue(shape, grid)
    return grid


def main(json_file):
    json_input = solutils.load_task(json_file)
    solution(json_input)


if __name__ == '__main__':
    main(sys.argv[1])

def border_points(position, gsize):
    """Returns a list of points that border the input position.
    position: (x,y) tuple for position coordinates
    gsize: tuple defining the grid size

    >>> side_borders((0, 2), (4,4))
    [(0, 1), (0, 3), (1, 2)]
    >>> side_borders((2, 2), (3,4))
    [(2, 1), (1, 2), (2, 3)]
    """

    x, y = position
    max_x, max_y = gsize
    # Convert grid to list positions
    max_x -= 1
    max_y -= 1
    # Validate input
    if x < 0 or x > max_x or y < 0 or y > max_y:
        print (f'Error, invalid parameters')
        return []
    raw_borders = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    borders = []
    for x,y in raw_borders:
        if x >=0 and x <= max_x and y >= 0 and y <= max_y:
            borders.append((x,y))
    return borders


def shapes(grid, border='side', colour=None):
    """Recognises shapes on the given grid, returns a list of shapes. Shape is
    recognised based on the defined border and colour
    grid: list of lists defining the grid values
    border: can be 'side' or 'diag'. 'side' will find shapes using only lateral
        borders, whereas 'diag' will also use diagonal positions as part of a
        shape
    colour: can be 'same', meaning use colour to also define the shape, if the
        colour in an adyacent position doesn't match it won't be considered part
        of the shape; defaults to None, colour not being considered to recognise
        a shape.
    """

    def find_shape(position, shapes):
        """Finds a shape given a position, returns a list with indices for all
        shapes that contained the point
        shapes: list containing all shapes"""

        indices = []
        for i in range(0, len(shapes)):
            if position in shapes[i]:
                indices.append(i)
        return indices

    grid_size = ((len(grid[0]), len(grid)))
    shapes = []  # Start with an empty list of shapes
    borders = [] # Borders for each position
    # Main loop to connect positions into shapes, for each position
    # get its borders, then check if those exist in other shapes
    # then join the shapes found or create a new shape if not connected to any
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == 0: # empty position, go to next
                continue
            print(f'Point: ({x},{y})')
            borders = border_points((x, y), grid_size)
            matches = [] # shape matches for a position
            for position in borders:
                matches += find_shape(position, shapes)
            matches = list(set(matches))
            print(f'matches: {matches}')
            if len(matches) == 0: # not connected, new shape ?
                shapes.append([(x, y)])
            elif len(matches) == 1: # found a shape to join
                shapes[matches[0]].append((x, y))
            else: # found more than one shape, connect shapes and delete dups
                for i in matches[1:]:
                    print(f'i is: {i}')
                    shapes[matches[0]] += shapes[i]
                    del shapes[i]
                shapes[matches[0]].append((x, y))
            print(f'shapes: {shapes}')
    return shapes


if __name__ == 'main':
    side_borders((0, 2), (4,4))
    side_borders((3, 4), (3,3))
    side_borders((2, 2), (3,4))

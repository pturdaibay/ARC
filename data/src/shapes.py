def border_points(position, gsize, btype='all'):
    """Returns a list of points that border the input position.
    position: (x,y) tuple for position coordinates
    gsize: tuple defining the grid size
    btype: border type
            'side' considers only adyacent as border
            'diag' considers only diagonal as border
            'all'  considers both side and diagonal

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
    adya_borders = [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]
    diag_borders = [(x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)]
    borders = []
    if btype == 'side' or btype == 'all':
        for x,y in adya_borders:
            if x >=0 and x <= max_x and y >= 0 and y <= max_y:
                borders.append((x,y))
    if btype == 'diag' or btype == 'all':
        for x,y in diag_borders:
            if x >=0 and x <= max_x and y >= 0 and y <= max_y:
                borders.append((x,y))

    return borders


def shapes(grid, btype='side', colour=False):
    """Recognises shapes on the given grid, returns a list of shapes. Shape is
    recognised based on the defined border and colour
    grid: list of lists defining the grid values
    btype: can be 'side' or 'diag'. 'side' will find shapes using only lateral
        borders, whereas 'diag' will also use diagonal positions as part of a
        shape
    colour: boolean, used to request that colour must match when finding shapes
    """

    def colour_match(pos1, pos2):
        """Returns a boolean if the colour in both grid positions is the same"""
        x1, y1 = pos1
        x2, y2 = pos2
        return grid[y1][x1] == grid[y2][x2]

    def find_shape(position, shapes):
        """Finds a shape given a position, returns a list with indices for all
        shapes that contained the point and match the colour if required
        position: tuple containing x,y coordinates on the grid
        shapes: list of lists containing all shapes"""

        indices = []
        for i in range(0, len(shapes)):
            if position in shapes[i]:
                if not colour:
                    indices.append(i)
                else:
                    if colour_match(position, shapes[i][0]):
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
            borders = border_points((x, y), grid_size, btype)
            matches = [] # shape matches for a position
            for position in borders:
                matches += find_shape(position, shapes)
            matches = list(set(matches))
            if len(matches) == 0: # not connected, new shape ?
                shapes.append([(x, y)])
            elif len(matches) == 1: # found a shape to join
                shapes[matches[0]].append((x, y))
            else: # found more than one shape, connect shapes and delete dups
                for i in matches[1:]:
                    shapes[matches[0]] += shapes[i]
                    del shapes[i]
                shapes[matches[0]].append((x, y))
    return shapes


if __name__ == '__main__':
    side_borders((0, 2), (4,4))
    side_borders((3, 4), (3,3))
    side_borders((2, 2), (3,4))

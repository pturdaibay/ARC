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

    shapes = []

if __name__ == 'main':
    side_borders((0, 2), (4,4))
    side_borders((3, 4), (3,3))
    side_borders((2, 2), (3,4))

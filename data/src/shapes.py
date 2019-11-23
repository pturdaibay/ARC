def side_borders(position, gsize):
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

if __name__ == 'main':
    side_borders((0, 2), (4,4))
    side_borders((3, 4), (3,3))
    side_borders((2, 2), (3,4))

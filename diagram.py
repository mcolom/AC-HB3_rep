#!/usr/bin/env python3

"""
This script draws a diagram of what is thought to be the
front of the AC-HB3 3-pin connector.

License: GNU GPL3
Author: Miguel Colom
"""

import matplotlib.pyplot as plt

def add_hole(axes, x, y, radius, border):
    '''
    Draw a hole
    '''
    # Without border
    hole = plt.Circle((x, y), radius, linewidth=1, fill=False)
    axes.add_artist(hole)

    # With border
    hole = plt.Circle((x, y), radius + border, linewidth=1, fill=False)
    axes.add_artist(hole)

def add_line(axes, xy1, xy2):
    '''
    Draw a line
    '''
    line = plt.Line2D((xy1[0], xy2[0]), (xy1[1], xy2[1]), linewidth=2)
    axes.add_artist(line)


# We think these are the correct numbers
distance_to_limit = 1.0
hole_with_border_radius = 3.0 / 2
border = 0.2

figure, axes = plt.subplots()
axes.set_aspect(1)
plt.grid()

plt.xlim([-1, 10])
plt.ylim([-1, 10])


# Bottom limit
add_line(axes, (0, 0), (9, 0))

# Left limit
add_line(axes, (0, 0), (0, 5))

# Right limit
add_line(axes, (9, 0), (9, 5))

# Upper limit
add_line(axes, (0, 8), (9, 8))


# Diagonal upper limits
add_line(axes, (0, 5), (0+5, 5+5))
add_line(axes, (9, 5), (9-5, 5+5))

### Holes

# Bottom left
add_hole(axes,
            distance_to_limit + hole_with_border_radius,
            distance_to_limit + hole_with_border_radius,
            hole_with_border_radius, border)


# Bottom right
add_hole(axes,
            distance_to_limit + 2*hole_with_border_radius + distance_to_limit + hole_with_border_radius, 
            distance_to_limit + hole_with_border_radius,
            hole_with_border_radius, border)

# Upper
a = distance_to_limit + 2*hole_with_border_radius + distance_to_limit + hole_with_border_radius
y = ((a/2)**2 + (a/2)**2)**0.5 + distance_to_limit

add_hole(axes,
            3 + 1.5, 
            y,
            hole_with_border_radius, border)


plt.title('AC-HB3')
plt.savefig("diagram.jpg")

plt.show()

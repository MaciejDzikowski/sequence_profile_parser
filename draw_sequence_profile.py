"""
Script draws and saves sequence profile as .svg file
"""

import sys
import sequence_profile_io as spi

sys.path.append('/core')
from core.SvgViewport import SvgViewport
from core.styles import ColorRGB, color_by_name, colormap_by_name
from core.svg_elements import Text, SquaresGroup

file = './cyped.CYP109.profile'


if __name__ == "__main__":
    order, sequence, matrix = spi.parse_sequence_profile(file)
    drawing = SvgViewport("rectangles_group.svg",
                          -200,  # margin to show full amino acids' shortcuts
                          0,
                          24 * len(sequence) + 500,  # width + margin
                          24 * len(order))  # height
    cmap = colormap_by_name("magma", 0.0, 1.0)

    # drawing a group of squares
    x_data = []
    y_data = []
    colors = []
    for i in range(len(sequence)):
        for j in range(len(order)):
            x_data.append(i * 24 + 40)
            # '40' to create space for amino acids' shortcuts
            y_data.append(j * 24)
            colors.append(cmap.color(matrix[j][i]))
    gid = 'squaresgroup'
    r = SquaresGroup(gid, x_data, y_data, colors, a=20)
    r.stroke = 'Grey'
    drawing.draw(r)

    # drawing an order
    for i in range(len(order)):
        text = Text(str(order[i]))
        text.x = 0
        text.y = 24 * i + 6  # '6' to center the shortcuts
        color = color_by_name("SteelBlue")
        stroke = color_by_name("SteelBlue").create_darker(0.3)
        text.fill, text.stroke, text.stroke_width = color, stroke, 0.3
        text.font_size = 20
        drawing.draw(text)

    # drawing a sequence
    for i in range(len(sequence)):
        text = Text(str(sequence[i]))
        text.x = 40 + 24 * i  # '40' to match sequence to squares
        text.y = len(order) * 24 - 4 + 6  # squares' width + '6' to match seq
        color = color_by_name("SteelBlue")
        stroke = color_by_name("SteelBlue").create_darker(0.3)
        text.fill, text.stroke, text.stroke_width = color, stroke, 0.3
        text.font_size = 12
        drawing.draw(text)

    drawing.close()

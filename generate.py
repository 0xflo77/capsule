import csv
import logging
import os
from colour import Color

# Configure logging
logging.basicConfig(filename='svg_generation.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
                    
# Function to calculate luminance of a color, prepending "#" to the hex value
def luminance(hex_color):
    color = Color(f"#{hex_color}")  
    rgb = [color.red, color.green, color.blue]
    return 0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2]

# Read colors from CSV
colors = []
with open('colors.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        colors.append(row[0])  # each row contains a single hex color code

# Sort colors by luminance
colors_sorted = sorted(colors, key=luminance)

# Determine the next available directory name
i = 1
while os.path.exists(f'set{i}'):
    i += 1
new_dir = f'set{i}'
os.makedirs(new_dir)


# Split into darker and lighter halves for base/top and eyelids
dark_colors = colors_sorted[:40]
light_colors = colors_sorted[40:]

# Generate 80 SVG files
for i in range(80):
    base_top_color = dark_colors[i % len(dark_colors)]
    eyelid_color = light_colors[i % len(light_colors)]

    
    svg_content = f'''<?xml version="1.0" encoding="utf-8"?>
<svg width="800px" height="800px" viewBox="0 0 800 800" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <path d="M800 0L800 0L800 800L0 800L0 0L800 0Z" id="path_1" />
        <clipPath id="clip_1">
            <use xlink:href="#path_1" clip-rule="evenodd" fill-rule="evenodd" />
        </clipPath>
    </defs>

    <g id="capsule-final">
        <path d="M800 0L800 0L800 800L0 800L0 0L800 0Z" id="capsule-final" fill="none" stroke="none" />
        <path d="M600 502C600 556.124 555.228 600 500 600L300 600C244.772 600 200 556.124 200 502L600 502Z" id="Base" fill="{'#' + base_top_color}" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
        <path d="M300 500C355.228 500 400 455.228 400 400L300 400L300 500L300 500Z" id="iris1R" fill="#000000" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
        <path d="M500 500C555.228 500 600 455.228 600 400L500 400L500 500L500 500Z" id="iris2R" fill="#000000" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
        <path d="M400 400C400 455.228 444.772 500 500 500L500 400L400 400L400 400Z" id="iris2L" fill="#FFFFFF" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
        <path d="M200 400C200 455.228 244.772 500 300 500L300 400L200 400L200 400Z" id="iris1L" fill="#FFFFFF" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
        <g id="REyelid" transform="translate(400 300)" clip-path="url(#clip_1)">
            <path d="M100 0C44.7715 0 0 44.7715 0 100L200 100C200 44.7715 155.228 0 100 0L100 0Z" id="Eyelid" fill="{'#' + eyelid_color}" fill-rule="evenodd" stroke="#000000" stroke-width="0" />
        </g>
        <path d="M300 300C355.228 300 400 344.771 400 400L200 400L200 300L300 300L300 300Z" id="LEyelid" fill="{'#' + eyelid_color}" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
        <path d="M600 298C600 243.876 555.228 200 500 200L300 200C244.772 200 200 243.876 200 298L600 298Z" id="Top" fill="{'#' + base_top_color}" fill-rule="evenodd" stroke="#000000" stroke-width="0" clip-path="url(#clip_1)" />
    </g>
</svg>
    '''

    # Save the SVG file
    filename = os.path.join(new_dir, f"svg_variant_{i+1}.svg")
    with open(filename, 'w') as file:
        file.write(svg_content)
    # Log work
    logging.info(f'Generated {filename} with base/top color #{base_top_color} and eyelid color #{eyelid_color}')

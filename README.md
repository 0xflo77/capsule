## SVG Color Variation Project
This project involves generating SVG files with specific color constraints for base and eyelid elements, creating an HTML gallery to display these SVGs, and displaying each SVG's base and eyelid colors along with the file name in the gallery.

## Overview
The project includes:

Generating SVG files with unique colors for base/top and eyelids, ensuring high contrast and no color repeats.
Creating an HTML gallery to display the generated SVG files.
Extracting and displaying color information (for base and eyelid) and file names in the HTML gallery.
Generating SVG Files
SVG files were generated with specific color constraints:

- Base/top and eyelids were assigned colors ensuring high contrast.
- Colors were selected to avoid repeats and ensure variety across SVGs.
- Python scripts were used for generating SVG files, calculating color luminance, sorting colors, and selecting colors based on specified constraints.

## Key Functions
- luminance(hex_color): Calculates the luminance of a color to facilitate sorting.
- generate_svg(base_top_color, eyelid_color, variation_number, directory): Generates an SVG file with specified colors for base/top and eyelids.
- Creating an HTML Gallery
An HTML gallery was created to display the generated SVGs. Additional functionality was implemented to parse SVG files, extract color information, and display it alongside each SVG in the gallery.

## HTML Gallery Features
- Displays each SVG with a specified width and height.
- Shows the base and eyelid colors below each SVG.
- Includes the file name for each SVG in the display.

## Style Adjustments
CSS styles were applied to ensure the gallery is visually appealing and the text displaying color information and file names is appropriately sized.

## Code Organization
The project's code is organized into separate functions and scripts to handle different aspects of the workflow, including SVG generation, color sorting and selection, and HTML gallery creation.

## Summary
This project demonstrates the automated generation of SVG files with color constraints and the creation of an HTML gallery to display these files with relevant color and file name information. Python scripts were used extensively for automation, with additional styling applied through CSS for the HTML gallery.

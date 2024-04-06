import csv
from colour import Color

# Function to calculate luminance
def luminance(hex_color):
    color = Color(f"#{hex_color}")
    return 0.2126 * color.red + 0.7152 * color.green + 0.0722 * color.blue

# Read colors from the CSV file
colors = []
with open('colors.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        colors.append(row[0])

# Sort colors by their luminance
colors_sorted = sorted(colors, key=luminance)

# Split colors into dark and light
dark_colors = colors_sorted[:40]
light_colors = colors_sorted[40:]

# HTML template with corrected CSS for escaping curly braces
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Color Visualization</title>
    <style>
        body {{ font-family: Arial, sans-serif; }}
        .row {{ display: flex; flex-wrap: wrap; }}
        .color-swatch {{ width: 60px; height: 60px; display: inline-block; margin: 5px; }}
        .color-info {{ display: none; }} /* Hide color info to fit everything in one page */
    </style>
</head>
<body>
    <h2>Dark Colors</h2>
    <div class="row">
        {dark_colors_html}
    </div>
    <h2>Light Colors</h2>
    <div class="row">
        {light_colors_html}
    </div>
</body>
</html>
'''

# Function to generate HTML for color swatches
def generate_color_html(color_list):
    html = ''
    for color in color_list:
        html += f'<div class="color-swatch" style="background-color: #{color};"></div>'
    return html

# Generating HTML content for dark and light colors
dark_colors_html = generate_color_html(dark_colors)
light_colors_html = generate_color_html(light_colors)

# Compiling final HTML content
html_content = html_template.format(dark_colors_html=dark_colors_html, light_colors_html=light_colors_html)

# Saving the HTML file
with open('color_visualization.html', 'w') as file:
    file.write(html_content)

print("HTML color visualization generated as 'color_visualization.html'.")

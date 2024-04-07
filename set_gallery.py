import os
import xml.etree.ElementTree as ET

set_directories = [d for d in os.listdir() if d.startswith('set') and os.path.isdir(d)]
latest_set_dir = sorted(set_directories)[-1]  # Latest set

# Start of the HTML document with updated styles for smaller text
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SVG Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .gallery { display: flex; flex-wrap: wrap; padding: 4px; }
        .gallery div { margin: 4px; text-align: center; }
        .gallery img { border: 1px solid #ccc; }
        .gallery img:hover { border-color: #777; }
        .color-info { font-size: 0.8em; } /* Smaller text for color information */
    </style>
</head>
<body>
    <h2>SVG Gallery</h2>
    <div class="gallery">
'''

# Processing SVG files and updating HTML content
svg_files = [f for f in os.listdir(latest_set_dir) if f.endswith('.svg')]
for svg_file in svg_files:
    tree = ET.parse(os.path.join(latest_set_dir, svg_file))
    root = tree.getroot()

    base_fill = root.find(".//*[@id='Base']")
    eyelid_fill = root.find(".//*[@id='Eyelid']")
    base_color = base_fill.get('fill') if base_fill is not None else 'N/A'
    eyelid_color = eyelid_fill.get('fill') if eyelid_fill is not None else 'N/A'

    html_content += f'''
        <div>
            <img src="{latest_set_dir}/{svg_file}" width="100" height="100">
            <div class="color-info">Base: {base_color}</div>
            <div class="color-info">Eyelid: {eyelid_color}</div>
        </div>\n'''

# End of the HTML document and writing to file
html_content += '''
    </div>
</body>
</html>
'''

with open('svg_gallery.html', 'w') as file:
    file.write(html_content)

print(f"Gallery HTML generated as 'svg_gallery.html', displaying SVGs from '{latest_set_dir}'.")

import os

set_directories = [d for d in os.listdir() if d.startswith('set') and os.path.isdir(d)]
latest_set_dir = sorted(set_directories)[-1]  # latest set

# Collect all SVG filenames in the directory
svg_files = [f for f in os.listdir(latest_set_dir) if f.endswith('.svg')]

# Start of the HTML document
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>SVG Gallery</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .gallery { display: flex; flex-wrap: wrap; padding: 4px; }
        .gallery img { margin: 4px; border: 1px solid #ccc; }
        .gallery img:hover { border-color: #777; }
    </style>
</head>
<body>
    <h2>SVG Gallery</h2>
    <div class="gallery">
'''

# Add each SVG file to the HTML content
for svg_file in svg_files:
    html_content += f'        <img src="{latest_set_dir}/{svg_file}" width="100" height="100">\n'

# End of the HTML document
html_content += '''
    </div>
</body>
</html>
'''

# Write the HTML content to a file
with open('svg_gallery.html', 'w') as file:
    file.write(html_content)

print(f"Gallery HTML generated as 'svg_gallery.html', displaying SVGs from '{latest_set_dir}'.")

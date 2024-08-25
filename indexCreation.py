import os
import html

def generate_index_html(directory):
    # Get all HTML files in the directory
    html_files = [f for f in os.listdir(directory) if f.endswith('.html') and f != 'index.html']
    
    # Sort the files alphabetically
    html_files.sort()
    
    # Generate the HTML content
    content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Notes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-size: 14pxl
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin-bottom: 10px;
        }
        a {
            color: #3498db;
            text-decoration: none;
            transition: color 0.3s ease;
        }
        a:hover {
            color: #2980b9;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Notes</h1>
    <ul>
"""
    
    # Add links to the HTML content
    for file in html_files:
        name = os.path.splitext(file)[0].replace('_', ' ').title()
        content += f'        <li><a href="{html.escape(file)}">{html.escape(name)}</a></li>\n'
    
    content += """
    </ul>
</body>
</html>
"""
    
    # Write the content to index.html
    with open(os.path.join(directory, 'index.html'), 'w') as f:
        f.write(content)

# Usage
generate_index_html('/home/mklno/myNotes')
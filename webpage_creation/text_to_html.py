import os
from xml.etree import ElementTree as ET

def txt_to_html(txt_file, html_file):
    """
    Converts a text file with multiple headers and paragraphs to an HTML file.
    
    Args:
        txt_file (str): Path to the text file.
        html_file (str): Path to the output HTML file.
    """
    # Read text file content
    with open(txt_file, 'r') as f:
        content = f.read()

    # Split the content into articles based on a blank line
    articles = content.split('\n\n')  # Assuming each article is separated by a blank line

    # Create root element for HTML
    root = ET.Element("html")

    # Create head and body elements
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    body = ET.SubElement(root, "body")

    # Loop through each article to create HTML content
    for article in articles:
        lines = article.strip().split('\n')
        if len(lines) > 1:  # Check if there is at least a title and some content
            h1 = ET.SubElement(body, "h1")
            h1.text = lines[0].strip()  # First line is the header
            p = ET.SubElement(body, "p")
            p.text = " ".join(lines[1:]).strip()  # Rest is the paragraph

    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8', xml_declaration=True)

def process_all_txt_files(directory):
    """
    Processes all txt files in the specified directory to convert them to HTML files.
    
    Args:
        directory (str): Directory containing the txt files.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            txt_file = os.path.join(directory, filename)
            html_file = os.path.join(directory, filename.replace('.txt', '.html'))
            txt_to_html(txt_file, html_file)
            print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")

# Specify the directory containing your txt files
directory = "./"
process_all_txt_files(directory)

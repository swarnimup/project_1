import os
from xml.etree import ElementTree as ET
import re

def create_html_element(body, tag, text, attrib={}):
    element = ET.SubElement(body, tag, attrib)
    element.text = text
    return element

def txt_to_html(directory, html_file):
    """
    Converts text files in the given directory with multiple headers and paragraphs to a single HTML file.
    
    Args:
        directory (str): Directory containing the txt files.
        html_file (str): Path to the output HTML file.
    """
    # Create root element for HTML
    root = ET.Element("html")
    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "News Aggregation Site"
    body = ET.SubElement(root, "body")
    
    # Process each text file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            txt_file = os.path.join(directory, filename)
            
            # Read text file content
            with open(txt_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Split the content into articles based on blank lines between articles
            articles = re.split(r'\n{2,}', content)
            
            # Process each article
            for article in articles:
                lines = article.strip().split('\n')
                if not lines:
                    continue
                
                # Extract and create the headline and article date
                headline = lines[0]
                date_info = lines[1] if len(lines) > 1 else ""
                create_html_element(body, "h2", headline)
                create_html_element(body, "h3", date_info)
                
                # Combine the rest as the main content
                paragraph = '\n'.join(lines[2:])  # Join remaining lines as paragraph
                create_html_element(body, "p", paragraph)
    
    # Write HTML tree to file
    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8', xml_declaration=True)

# Specify the directory containing your txt files and the output HTML file path
directory = "./Input_txtfiles/"
html_file = "all_news_articles.html"
txt_to_html(directory, html_file)

print(f"All text files in '{directory}' have been converted to a single HTML file '{html_file}'.")

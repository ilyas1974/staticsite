import re

def extract_markdown_images(text):
    # Matches ![alt](url)
    pattern = r"!\[([^\[\]]*)\]\(([^()]+)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    # Matches [text](url) but not ![alt](url)
# Matches [text](url) but not ![alt](url)
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^()]+)\)"
    return re.findall(pattern, text)

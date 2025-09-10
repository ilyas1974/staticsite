import re

# Import or define TextType and TextNode before using them
from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    image_pattern = r"!\[([^\]]+)\]\((https?://[^\)]+)\)"
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(image_pattern, node.text)
        i = 0
        while i < len(parts):
            if i + 2 < len(parts):  # found an image match
                text_before = parts[i]
                if text_before:
                    new_nodes.append(TextNode(text_before, TextType.TEXT))
                image_alt = parts[i + 1]
                image_url = parts[i + 2]
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
                i += 3
            else:
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                i += 1
    return new_nodes

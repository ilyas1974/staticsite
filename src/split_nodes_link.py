import re
from textnode import TextNode, TextType

def split_nodes_link(old_nodes):
    new_nodes = []
    link_pattern = r"\[([^\]]+)\]\((https?://[^\)]+)\)"
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(link_pattern, node.text)
        i = 0
        while i < len(parts):
            if i + 2 < len(parts):  # found a link match
                text_before = parts[i]
                if text_before:
                    new_nodes.append(TextNode(text_before, TextType.TEXT))
                link_text = parts[i + 1]
                link_url = parts[i + 2]
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                i += 3
            else:
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
                i += 1
    return new_nodes

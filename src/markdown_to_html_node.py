import re
from split_blocks import split_blocks
from htmlnode import HTMLNode 
from textnode import TextNode
from text_parser import text_to_children   
from text_node_to_html_node import text_node_to_html_node
from leafnode import LeafNode  # Make sure this import path is correct

def block_to_block_type(block: str) -> str:
    block = block.strip()
    if block.startswith("```"):
        return "code"
    elif block.startswith(">"):
        return "quote"
    elif block.startswith("#"):
        return "heading"
    elif block.startswith(("-", "*", "+")):
        return "unordered_list"
    elif re.match(r'^\d+\.\s', block.strip()):
        return "ordered_list"
    else:
        return "paragraph"

def heading_level(block: str) -> int:
    """Returns the heading level (number of leading #) for a Markdown heading block."""
    return len(block) - len(block.lstrip("#"))

def strip_heading_syntax(block: str) -> str:
    """Removes leading '#' characters and whitespace from a heading block."""
    return block.lstrip("#").lstrip()

def strip_quote_syntax(block: str) -> str:
    """Removes leading '>' and whitespace from a quote block."""
    return block.lstrip(">").lstrip()

def extract_list_items(block: str) -> list:
    lines = block.strip().split('\n')
    items = []
    for line in lines:
        stripped = line.lstrip()
        # Unordered list
        if stripped.startswith(("-", "*", "+")):
            item = stripped[1:].lstrip()
            items.append(item)
        # Ordered list using regex
        elif re.match(r'^\d+\.\s+', stripped):
            item = re.sub(r'^\d+\.\s+', '', stripped)
            items.append(item)
    return items


def strip_code_syntax(block: str) -> str:
    """
    Removes the leading and trailing triple backticks from a code block.
    """
    lines = block.strip().split('\n')
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, children=children, props=props)

    def to_html(self) -> str:
        # Render children recursively
        children_html = ''.join(child.to_html() for child in self.children)

        # Render props as HTML attributes
        props_str = ''
        if self.props:
            props_str = ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"

def text_nodes_to_html_nodes(text_nodes: list) -> list:
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = split_blocks(markdown)  # Step 1: use existing block splitter
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)  # Step 2: identify type

        if block_type == "paragraph":
            text_nodes = text_to_children(block)
            html_nodes = text_nodes_to_html_nodes(text_nodes)
            children.append(ParentNode("p", children=html_nodes))

        elif block_type == "heading":
            level = heading_level(block)
            text_nodes = text_to_children(strip_heading_syntax(block))
            html_nodes = text_nodes_to_html_nodes(text_nodes)
            children.append(ParentNode(f"h{level}", children=html_nodes))

        elif block_type == "quote":
            quote_text = strip_quote_syntax(block)
            text_nodes = text_to_children(quote_text)
            html_nodes = text_nodes_to_html_nodes(text_nodes)
            children.append(ParentNode("blockquote", children=html_nodes))

        elif block_type == "unordered_list":
            items = extract_list_items(block)
            list_nodes = [
                ParentNode("li", children=text_nodes_to_html_nodes(text_to_children(item)))
                for item in items
        ]
            children.append(ParentNode("ul", children=list_nodes))

        elif block_type == "ordered_list":
            items = extract_list_items(block)
            list_nodes = [
                ParentNode("li", children=text_nodes_to_html_nodes(text_to_children(item)))
                for item in items
            ]
            children.append(ParentNode("ol", children=list_nodes))

        elif block_type == "code":
            code_text = strip_code_syntax(block)
            text_node = TextNode(code_text, "code")
            code_node = text_node_to_html_node(text_node)
            children.append(ParentNode("pre", children=[code_node]))

        else:
            # fallback to paragraph if unknown
            text_nodes = text_to_children(block)
            html_nodes = text_nodes_to_html_nodes(text_nodes)
            children.append(ParentNode("p", children=html_nodes))

    return ParentNode("div", children=children)

if __name__ == "__main__":
    with open("content/index.md") as f:
        markdown = f.read()
    blocks = split_blocks(markdown)
    for i, block in enumerate(blocks):
        print(f"\nBlock {i}:\n{block}")
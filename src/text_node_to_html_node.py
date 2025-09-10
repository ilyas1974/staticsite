from leafnode import LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    else:
        return LeafNode(None, text_node.text)


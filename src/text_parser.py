import re
from textnode import TextNode, TextType
from leafnode import LeafNode


def text_to_children(text: str) -> list[TextNode]:
    nodes = []
    pattern = r'(\*\*[^*]+\*\*|\*[^*]+\*|\[([^\]]+)\]\(([^)]+)\))'
    pos = 0

    for match in re.finditer(pattern, text):
        start, end = match.span()

        # Add plain text before match
        if start > pos:
            nodes.append(TextNode(text[pos:start], "text"))

        matched_text = match.group(0)

        if matched_text.startswith("**"):
            nodes.append(TextNode(matched_text[2:-2], "bold"))
        elif matched_text.startswith("*"):
            nodes.append(TextNode(matched_text[1:-1], "italic"))
        elif matched_text.startswith("["):
            label = match.group(2)
            url = match.group(3)
            nodes.append(TextNode(label, "link", url=url))

        pos = end

    # Add remaining plain text
    if pos < len(text):
        nodes.append(TextNode(text[pos:], "text"))

    return nodes

if __name__ == "__main__":
    sample = "This is **bold**, _italic_, and `code`."
    for node in text_to_children(sample):
        print(node)

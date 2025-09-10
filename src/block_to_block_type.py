import re
from blocktype_enum import BlockType

def block_to_block_type(block):
    lines = block.split("\n")

    # Code block
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Heading
    if re.match(r"#{1,6} ", lines[0]):
        return BlockType.HEADING

    # Quote block
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list
    if all(re.match(r"-\s+", line) for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list
    for i, line in enumerate(lines):
        expected_prefix = f"{i+1}. "
        if not line.startswith(expected_prefix):
            break
    else:
        return BlockType.ORDERED_LIST

    # Default: Paragraph
    return BlockType.PARAGRAPH

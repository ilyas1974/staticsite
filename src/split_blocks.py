def split_blocks(markdown: str) -> list[str]:
    lines = markdown.split('\n')
    blocks = []
    current_block = []

    for line in lines:
        # Trim any trailing spaces to normalize
        line = line.rstrip()

        if line == "":
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
        else:
            current_block.append(line)

    # Add last block if it exists
    if current_block:
        blocks.append('\n'.join(current_block))

    return blocks

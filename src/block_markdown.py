

def markdown_to_blocks(markdown):
    block_strings = []
    potential_blocks = markdown.split("\n\n")
    for potential_block in potential_blocks:
        if potential_block != '':
            potential_block = potential_block.strip()
            block_strings.append(potential_block)
    return block_strings

import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_blocks(self):
        md = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n"
            "- This is the first list item\n- This is a list item\n- This is another list item"
        )
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item\n- This is a list item\n- This is another list item"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_extra_spacing(self):
        md = "\n\n\nThis is a block\n\n\n\nAnother block\n\n\n"
        expected = [
            "This is a block",
            "Another block"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_inline_newlines(self):
        md = (
            "This is the first paragraph line\n"
            "Still same paragraph\n\n"
            "Second paragraph starts\n"
            "Continues here"
        )
        expected = [
            "This is the first paragraph line\nStill same paragraph",
            "Second paragraph starts\nContinues here"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

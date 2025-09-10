import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_full_conversion(self):
        input_text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        result = text_to_textnodes(input_text)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(result, expected)

    def test_no_markup(self):
        input_text = "Just plain text."
        result = text_to_textnodes(input_text)
        expected = [TextNode("Just plain text.", TextType.TEXT)]
        self.assertListEqual(result, expected)

    def test_nested_markup(self):
        input_text = "**_bold and italic_**"
        result = text_to_textnodes(input_text)
        expected = [
            TextNode("bold and italic", TextType.BOLD),  # still split at ** first
        ]
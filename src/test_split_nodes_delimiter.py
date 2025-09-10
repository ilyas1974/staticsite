import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_code_delimiter(self):
        node = TextNode("This has `inline code` wrapped", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This has ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
            TextNode(" wrapped", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_multiple_code_delimiters(self):
        node = TextNode("`first` and `second` code", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("first", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.CODE),
            TextNode(" code", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_bold_double_asterisks(self):
        node = TextNode("This is **bolded** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bolded", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_single_underscore(self):
        node = TextNode("This _italic_ style", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" style", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This has `unmatched code", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [node])

    def test_non_text_nodes_unchanged(self):
        non_text = TextNode("Don't touch me", TextType.BOLD)
        result = split_nodes_delimiter([non_text], "`", TextType.CODE)
        self.assertEqual(result, [non_text])

if __name__ == "__main__":
    unittest.main()

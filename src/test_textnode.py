import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_different_text(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_neq_different_type(self):
        node1 = TextNode("Sample text", TextType.BOLD)
        node2 = TextNode("Sample text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_neq_different_url(self):
        node1 = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.LINK, "https://boot.dev")
        self.assertNotEqual(node1, node2)

    def test_eq_url_none(self):
        node1 = TextNode("Some text", TextType.TEXT, None)
        node2 = TextNode("Some text", TextType.TEXT)  # Implicit None
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()
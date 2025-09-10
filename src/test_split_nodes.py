import unittest
from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link


def test_split_nodes_link(self):
    node = TextNode("Click [here](https://example.com) and [there](https://another.com)", TextType.TEXT)
    result = split_nodes_link([node])
    expected = [
        TextNode("Click ", TextType.TEXT),
        TextNode("here", TextType.LINK, "https://example.com"),
        TextNode(" and ", TextType.TEXT),
        TextNode("there", TextType.LINK, "https://another.com")
    ]
    self.assertListEqual(result, expected)

def test_split_nodes_image(self):
    node = TextNode("An image ![alt text](https://img.com/pic.png) and ![second](https://img.com/second.png)", TextType.TEXT)
    result = split_nodes_image([node])
    expected = [
        TextNode("An image ", TextType.TEXT),
        TextNode("alt text", TextType.IMAGE, "https://img.com/pic.png"),
        TextNode(" and ", TextType.TEXT),
        TextNode("second", TextType.IMAGE, "https://img.com/second.png")
    ]
    self.assertListEqual(result, expected)

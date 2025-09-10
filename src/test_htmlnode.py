import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_multiple(self):
        node = HTMLNode(tag="a", props={"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_props_to_html_empty(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_repr_output(self):
        node = HTMLNode(tag="h1", value="Welcome", props={"class": "header"})
        expected = 'HTMLNode(tag=h1, value=Welcome, children=[], props={\'class\': \'header\'})'
        self.assertEqual(repr(node), expected)

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click here", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click here</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just plain text")
        self.assertEqual(node.to_html(), "Just plain text")

    def test_leaf_missing_value_raises(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)



class TestParentNode(unittest.TestCase):

    def test_to_html_with_multiple_children(self):
        children = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ]
        node = ParentNode("p", children)
        expected_html = "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_nested_parents(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_no_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "hello")])

    def test_no_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)


if __name__ == "__main__":
    unittest.main()

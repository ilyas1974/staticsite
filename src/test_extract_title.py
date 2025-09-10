import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_whitespace(self):
        self.assertEqual(extract_title("   #   Hello World   "), "Hello World")

    def test_multiple_lines(self):
        markdown = """Some text
# First Title
## Subtitle
"""
        self.assertEqual(extract_title(markdown), "First Title")

    def test_no_title_raises(self):
        with self.assertRaises(Exception):
            extract_title("## Not an H1\nSome paragraph")

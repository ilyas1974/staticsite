import unittest
from extractor import extract_markdown_images, extract_markdown_links

class TestExtractor(unittest.TestCase):

    def test_single_image(self):
        text = "Here is an image ![alt text](https://img.com/cat.png)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("alt text", "https://img.com/cat.png")])

    def test_multiple_images(self):
        text = "![one](url1) some text ![two](url2)"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("one", "url1"), ("two", "url2")])

    def test_single_link(self):
        text = "Visit [Boot.dev](https://www.boot.dev) now!"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("Boot.dev", "https://www.boot.dev")])

    def test_multiple_links(self):
        text = "[A](urlA) and [B](urlB)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("A", "urlA"), ("B", "urlB")])

    def test_link_and_image_combo(self):
        text = "![img](imgURL) and [link](linkURL)"
        img_result = extract_markdown_images(text)
        link_result = extract_markdown_links(text)
        self.assertEqual(img_result, [("img", "imgURL")])
        self.assertEqual(link_result, [("link", "linkURL")])

    def test_invalid_markdown(self):
        text = "This is [broken](not_closed"
        self.assertEqual(extract_markdown_links(text), [])
        self.assertEqual(extract_markdown_images(text), [])

if __name__ == "__main__":
    unittest.main()

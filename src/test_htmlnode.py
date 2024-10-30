import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_repr_1(self):
        node = HTMLNode("a", "sample link", None, {"href": "https://www.google.com"})
        repr_str = "HTMLNode(a, sample link, None, {'href': 'https://www.google.com'})"
        self.assertEqual(str(node), repr_str)

    def test_props_to_html_1(self):
        node = HTMLNode("a", "sample link", None, {"href": "https://www.google.com", "second":"text"})
        props_str = '''href="https://www.google.com" second="text"'''
        self.assertEqual(node.props_to_html(), props_str)

    def test_repr_2(self):
        fake_child = HTMLNode("a", "sample child", None, {"href": "https://www.google.com"})
        node = HTMLNode("p", "sample", fake_child, None)
        repr_str = "HTMLNode(p, sample, HTMLNode(a, sample child, None, {'href': 'https://www.google.com'}), None)"
        self.assertEqual(str(node), repr_str)


if __name__ == "__main__":
    unittest.main()
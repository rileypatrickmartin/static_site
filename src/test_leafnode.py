import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html_1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), html)

    def test_to_html_2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        html = '''<a href="https://www.google.com">Click me!</a>'''
        self.assertEqual(node.to_html(), html)

    def test_no_value(self):
        node = LeafNode("a", None)
        self.assertRaises(ValueError, node.to_html)   

    def test_no_tag(self):
        node = LeafNode(None, "Didn't need it anyways")
        self.assertEqual(node.to_html(), "Didn't need it anyways")          
        

if __name__ == "__main__":
    unittest.main()
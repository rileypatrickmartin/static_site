import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):

    def test_to_html_1(self):
        node = ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )

        html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html)

    # def test_to_html_2(self):
    #     node = ParentNode("a", "Click me!", {"href": "https://www.google.com"})
    #     html = '''<a href="https://www.google.com">Click me!</a>'''
    #     self.assertEqual(node.to_html(), html)

    def test_no_children(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)   

    def test_no_tag(self):
        node = ParentNode(None, [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ])
        self.assertRaises(ValueError, node.to_html) 
    


    # Test all the edge cases you can think of, 
    # including nesting ParentNode objects inside of one another, 
    # multiple children, and no children. 
    def test_to_html_2(self):
        node = ParentNode(
                    "p",
                    [
                        ParentNode(
                                    "p",
                                    [
                                        LeafNode("b", "Bold text"),
                                        LeafNode(None, "Normal text"),
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Normal text"),
                                    ],
                                ),
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )

        html = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html)        
        

if __name__ == "__main__":
    unittest.main()
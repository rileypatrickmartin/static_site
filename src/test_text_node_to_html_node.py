import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from main import text_node_to_html_node
from unittest.mock import Mock


class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_node_to_html_node_normal(self):
        text_node = TextNode("Text", TextType.TEXT)
        leaf_node = LeafNode(None, "Text")
        self.assertEqual(text_node_to_html_node(text_node), leaf_node)

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Text", TextType.BOLD)
        leaf_node = LeafNode("b", "Text")
        self.assertEqual(text_node_to_html_node(text_node), leaf_node)

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Text", TextType.ITALIC)
        leaf_node = LeafNode("i", "Text")
        self.assertEqual(text_node_to_html_node(text_node), leaf_node)

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Text", TextType.CODE)
        leaf_node = LeafNode("code", "Text")
        self.assertEqual(text_node_to_html_node(text_node), leaf_node)

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Text", TextType.LINK, "www.google.com")
        leaf_node = LeafNode("a", "Text", props={'href':'www.google.com'})
        self.assertEqual(text_node_to_html_node(text_node), leaf_node)

    def test_text_node_to_html_node_images(self):
        text_node = TextNode("Text", TextType.IMAGES, "www.google.com")
        leaf_node = LeafNode("img", "", props={'alt':"Text", 'src':'www.google.com'})
        self.assertEqual(text_node_to_html_node(text_node), leaf_node)

    def test_text_node_to_html_node_not_in_enum(self):
        fake_enum = Mock()
        fake_enum.value = None 
        text_node = TextNode("Text", fake_enum)
        self.assertRaises(ValueError, text_node_to_html_node, text_node)   

from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from typing import List
import logging, sys

def main():
    a_textnode = TextNode("test", TextType.NORMAL, "www.google.com")
    print(a_textnode)

def text_node_to_html_node(text_node)->LeafNode:
    if text_node.text_type == 'text':
        return LeafNode(None, text_node.text)

    if text_node.text_type == 'bold':
        return LeafNode("b", text_node.text)

    if text_node.text_type == 'italic':
        return LeafNode("i", text_node.text)

    if text_node.text_type == 'code':
        return LeafNode("code", text_node.text)
  
    if text_node.text_type == 'link':
        return LeafNode("a", text_node.text, props={'href':text_node.url})

    if text_node.text_type == 'images':
        return LeafNode("img", "", props={'alt':text_node.text,'src':text_node.url})

    raise ValueError("Text type of text node not in TextType Enum!")

if __name__ == '__main__':
    main()
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode

def main():
    a_textnode = TextNode("test", TextType.NORMAL, "www.google.com")
    print(a_textnode)

def text_node_to_html_node(text_node)->LeafNode:
    if text_node.text_type == 'normal':
        return LeafNode(None, text_node.value)

    if text_node.text_type == 'bold':
        return LeafNode("b", text_node.value)

    if text_node.text_type == 'italic':
        return LeafNode("i", text_node.value)

    if text_node.text_type == 'code':
        return LeafNode("code", text_node.value)
  
    if text_node.text_type == 'link':
        return LeafNode("a", text_node.value, props={'href':text_node.url})

    if text_node.text_type == 'images':
        return LeafNode("img", "", props={'alt':text_node.value,'src':text_node.url})

    raise Exception("Text type of text node not in TextType Enum!")

if __name__ == '__main__':
    main()
from textnode import TextType, TextNode

def main():
    a_textnode = TextNode("test", TextType.NORMAL, "www.google.com")
    print(a_textnode)

if __name__ == '__main__':
    main()
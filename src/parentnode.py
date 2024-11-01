from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children, None)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("There are no children!")

        return f"<{self.tag}>{''.join([node.to_html() for node in self.children])}</{self.tag}>"

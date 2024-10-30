from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag, None, children, None)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("There are no children!")
        # Otherwise, 
        # return a string representing the HTML tag of the node and its children. 
        # This should be a recursive method 
        #  (each recursion being called on a nested child node).
        # I iterated over all the children and called to_html on each,
        #  concatenating the results and injecting them 
        #  between the opening and closing tags of the parent.
        return f"<{self.tag}>{''.join([node.to_html() for node in self.children])}</{self.tag}>"

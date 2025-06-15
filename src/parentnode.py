from functools import reduce
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            ValueError("Parent Node must contain a tag")
        if self.children == None:
            ValueError("Parent Node must contain children")
        
        child_nodes = reduce(lambda acc, x: acc + x.to_html(), self.children, "")
        return f"<{self.tag}{self.props_to_html()}>{child_nodes}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
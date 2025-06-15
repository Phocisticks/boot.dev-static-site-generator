from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node must contain a value")
        
        if self.tag is not None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        
        return self.value

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
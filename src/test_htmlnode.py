import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            props={"href": "https://www.google.com","target": "_blank"}
        )
        
        actual = node.props_to_html()

        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected, actual)

    def test_props_to_html_empty_props(self):
        node = HTMLNode()
        
        actual = node.props_to_html()

        expected = ''
        self.assertEqual(expected, actual)
    
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
    
    def test_repr(self):
        node = HTMLNode(
            "a",
            "link to cool image",
            [],
            {"href": "https://www.google.com","target": "_blank"}
        )

        actual = repr(node)
        
        expected = "HTMLNode(a, link to cool image, [], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")

        actual = node.to_html()

        expected = "<p>Hello, world!</p>"
        self.assertEqual(actual, expected)
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        
        actual = node.to_html()

        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(actual, expected)
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        
        actual = node.to_html()

        expected = "Hello, world!"
        self.assertEqual(actual, expected)
    
    def test_leaf_no_value(self):
        node = LeafNode("p", None)

        self.assertRaises(ValueError, node.to_html)
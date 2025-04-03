import unittest

from src.html_nodes.text_node import (
    TextNode,
    TextType,
    text_node_to_html_node
)


class TestTextNode(unittest.TestCase):
    def test_text_node_eq(self):
        boldNode = TextNode(
            "This is a text node",
            TextType.BOLD.value
        )
        equalBoldNode = TextNode(
            "This is a text node",
            TextType.BOLD.value
        )
        diffTypeNode = TextNode(
            "This is a text node",
            TextType.NORMAL.value
        )
        diffTextNode = TextNode(
            "This is another text node",
            TextType.BOLD.value
        )
        boldNodeWithUrl = TextNode(
            "This is a text node",
            TextType.BOLD.value,
            "https://www.google.com"
        )
        equalBoldNodeWithUrl = TextNode(
            "This is a text node",
            TextType.BOLD.value,
            "https://www.google.com"
        )
        diffUrlNodeUrl = TextNode(
            "This is a text node",
            TextType.BOLD.value,
            "https://www.yahoo.com"
        )
        diffTypeNodeUrl = TextNode(
            "This is a text node",
            TextType.NORMAL.value,
            "https://www.google.com"
        )
        diffTextNodeUrl = TextNode(
            "This is another text node",
            TextType.BOLD.value,
            "https://www.google.com"
        )
        self.assertEqual(boldNode, equalBoldNode)
        self.assertEqual(boldNodeWithUrl, equalBoldNodeWithUrl)
        self.assertNotEqual(boldNode, boldNodeWithUrl)
        self.assertNotEqual(boldNode, diffTypeNode)
        self.assertNotEqual(boldNode, diffTextNode)
        self.assertNotEqual(boldNodeWithUrl, diffTypeNodeUrl)
        self.assertNotEqual(boldNodeWithUrl, diffTextNodeUrl)
        self.assertNotEqual(boldNode, boldNodeWithUrl)
        self.assertNotEqual(boldNodeWithUrl, diffUrlNodeUrl)

    def test_text_node_to_html(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(
            html_node.to_html(),
            "This is a text node"
        )

        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(
            html_node.to_html(),
            '<strong>This is a text node</strong>'
        )

        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(
            html_node.to_html(),
            '<em>This is a text node</em>'
        )

        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
        self.assertEqual(
            html_node.to_html(),
            '<code>This is code</code>'
        )

        node = TextNode("Google", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Google")
        self.assertEqual(html_node.props["href"], "https://www.google.com")
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://www.google.com">Google</a>'
        )

        node = TextNode("image", TextType.IMAGE, "image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "image.png")
        self.assertEqual(html_node.props["alt"], "image")
        self.assertEqual(
            html_node.to_html(),
            '<img src="image.png" alt="image"></img>'
        )


if __name__ == "__main__":
    unittest.main()

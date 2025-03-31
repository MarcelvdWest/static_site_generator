import unittest

from src.html_nodes.text_node import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()

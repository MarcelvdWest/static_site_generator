import unittest

from src.html_nodes.html_node import HTMLNode
from src.html_nodes.text_node import TextNode, TextType, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        self.assertEqual(
            HTMLNode(
                "<h1>", "value", "<p>", {"test": "testing"}
            ).props_to_html(),
            ' test="testing"'
        )
        self.assertEqual(
            HTMLNode(
                "<h1>",
                "value",
                "<p>",
                {
                    "test": "testing",
                    "test2": "testing2",
                    "test3": "testing3"
                }
            ).props_to_html(),
            ' test="testing" test2="testing2" test3="testing3"'
        )
        with self.assertRaises(TypeError):
            HTMLNode("<h1>", "value", "<p>").props_to_html()

    def test_to_html(self):
        with self.assertRaises(NotImplementedError):
            HTMLNode(None, None, None, None).to_html()

    def test_repr(self):
        self.assertEqual(
            HTMLNode(None, None, None, None).__repr__(),
            """HTMLNode(
            tag: no tag,
            content: no value,
            children: no children,
            props: no props
        )""")
        self.assertEqual(
            HTMLNode("<h1>", None, None, None).__repr__(),
            """HTMLNode(
            tag: <h1>,
            content: no value,
            children: no children,
            props: no props
        )""")
        self.assertEqual(
            HTMLNode(None, "value", None, None).__repr__(),
            """HTMLNode(
            tag: no tag,
            content: value,
            children: no children,
            props: no props
        )""")
        self.assertEqual(
            HTMLNode(None, None, "<p>", None).__repr__(),
            """HTMLNode(
            tag: no tag,
            content: no value,
            children: <p>,
            props: no props
        )""")
        self.assertEqual(
            HTMLNode(None, None, None, {"test": "testing"}).__repr__(),
            """HTMLNode(
            tag: no tag,
            content: no value,
            children: no children,
            props: {'test': 'testing'}
        )""")
        self.assertEqual(
            HTMLNode("<h1>", "value", "<p>", {"test": "testing"}).__repr__(),
            """HTMLNode(
            tag: <h1>,
            content: value,
            children: <p>,
            props: {'test': 'testing'}
        )""")


if __name__ == "__main__":
    unittest.main()

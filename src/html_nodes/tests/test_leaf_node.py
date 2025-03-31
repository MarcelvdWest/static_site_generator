import unittest

from src.html_nodes.leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        with self.assertRaises(ValueError):
            LeafNode(None, "<p>", None).to_html()

        self.assertEqual(
            LeafNode("Value", None, None).to_html(),
            "Value"
        )

        with self.assertRaises(ValueError):
            LeafNode(
                None,
                None,
                {"param": "value", "param2": "value2"}
            ).to_html()

        self.assertEqual(
            LeafNode("Value", "p", None).to_html(),
            "<p>Value</p>"
        )

        self.assertEqual(
            LeafNode(
                "Value",
                "p",
                {"param": "value", "param2": "value2"}
            ).to_html(),
            "<p param=value param2=value2>Value</p>"
        )

        self.assertEqual(
            LeafNode(
                "Value",
                None,
                {"param": "value", "param2": "value2"}
            ).to_html(),
            "Value"
        )

        self.assertEqual(
            LeafNode(
                2,
                "h2",
                {"param": "value", "param2": "value2"}
            ).to_html(),
            "<h2 param=value param2=value2>2</h2>"
        )


if __name__ == "__main__":
    unittest.main()

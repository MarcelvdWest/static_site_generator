import unittest

from src.html_nodes.leaf_node import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        with self.assertRaises(ValueError):
            LeafNode("<p>", None).to_html()

        self.assertEqual(
            LeafNode(None, "Value").to_html(),
            "Value"
        )

        with self.assertRaises(ValueError):
            LeafNode(
                None,
                None,
                {"param": "value", "param2": "value2"}
            ).to_html()

        self.assertEqual(
            LeafNode( "p", "Value", None).to_html(),
            "<p>Value</p>"
        )

        self.assertEqual(
            LeafNode(
                "p",
                "Value",
                {"param": "value", "param2": "value2"}
            ).to_html(),
            '<p param="value" param2="value2">Value</p>'
        )

        self.assertEqual(
            LeafNode(
                None,
                "Value",
                {"param": "value", "param2": "value2"}
            ).to_html(),
            "Value"
        )

        self.assertEqual(
            LeafNode(
                "h2",
                2,
                {"param": "value", "param2": "value2"}
            ).to_html(),
            '<h2 param="value" param2="value2">2</h2>'
        )


if __name__ == "__main__":
    unittest.main()

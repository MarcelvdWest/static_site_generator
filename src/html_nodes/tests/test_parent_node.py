import unittest

from src.html_nodes.parent_node import ParentNode
from src.html_nodes.leaf_node import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        params = {"margin": "15px"}
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node_with_params = ParentNode("div", [child_node], params)
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        self.assertEqual(
            parent_node_with_params.to_html(),
            '<div margin="15px"><span>child</span></div>'
        )

    def test_to_html_with_grandchildren(self):
        params = {"margin": "15px"}
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        parent_node_with_params = ParentNode("div", [child_node], params)
        child_node_with_params = ParentNode("span", [grandchild_node], params)
        parent_child_with_params = ParentNode("div", [child_node_with_params])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        self.assertEqual(
            parent_node_with_params.to_html(),
            '<div margin="15px"><span><b>grandchild</b></span></div>'
        )
        self.assertEqual(
            parent_child_with_params.to_html(),
            '<div><span margin="15px"><b>grandchild</b></span></div>'
        )

    def test_parent_to_html_with_inner_text(self):
        text_node_1 = LeafNode(None, "I am a ")
        text_node_2 = LeafNode(None, " of the child ")
        text_node_3 = LeafNode(None, ".")
        bold_node = LeafNode("strong", "grandchild")
        italic_node = LeafNode("em", "node")
        grandchild_node = ParentNode("span", [text_node_1, bold_node, text_node_2, italic_node, text_node_3])
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><p><span>I am a <strong>grandchild</strong> of the child <em>node</em>.</span></p></div>",
        )

    def test_parent_to_html_errors(self):
        with self.assertRaises(ValueError):
            # child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", None)
            parent_node.to_html()

        with self.assertRaises(ValueError):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()

        with self.assertRaises(ValueError):
            # child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, None)
            parent_node.to_html()

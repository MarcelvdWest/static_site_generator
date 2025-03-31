from typing import Any

from .html_node import HTMLNode
from .leaf_node import LeafNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict | None = None
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Instance has no tag value")

        if not self.children:
            raise ValueError("instance has no children value")

        html_str = f"<{self.tag}>"

        for child in self.children:

            if isinstance(child, LeafNode):
                return html_str + child.to_html()

            return html_str + child.to_html()

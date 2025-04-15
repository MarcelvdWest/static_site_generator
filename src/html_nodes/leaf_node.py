from .html_node import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict | None = None
    ):
        super().__init__(tag=tag, value=value, props=props)

    def __eq__(self, other_node: "LeafNode"):
        return self.tag == other_node.tag and self.value == other_node.value and self.props == other_node.props

    def to_html(self):
        if not isinstance(self.value, str | int):
            raise ValueError("instance of this class must contain a value")

        if not self.tag:
            return self.value

        props = ""
        if self.props:
            # print("Has Props")
            props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

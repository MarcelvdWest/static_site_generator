from .html_node import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag: str | None = None, props: dict | None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("instance of this class must contain a value")

        if not self.tag:
            return self.value

        props = ""
        if self.props:
            # print("Has Props")
            props = self.props_to_html()

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

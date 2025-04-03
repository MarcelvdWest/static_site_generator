from .html_node import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict | None = None
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag and not self.children:
            raise ValueError("Instance has no tag and no children value")

        if not self.tag:
            raise ValueError("Instance has no tag value")

        if not self.children:
            raise ValueError("instance has no children value")

        props = ""
        if self.props:
            props = self.props_to_html()

        html_str = f"<{self.tag}{props}>"

        for child in self.children:

            html_str = html_str + child.to_html()

        return f"{html_str}</{self.tag}>"

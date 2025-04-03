from typing import Any


class HTMLNode():
    def __init__(
        self,
        tag: str | None = None,
        value=None,
        children: Any | None = None,
        props: dict | None = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        # print(self.props)
        if self.props:
            props = self.props.copy()
            return " " + (" ".join([f'{key}="{props[key]}"' for key in props]))
        else:
            raise TypeError("There are no props")

    def __repr__(self):
        return f"""HTMLNode(
            tag: {self.tag if self.tag else 'no tag'},
            content: {self.value if self.value else 'no value'},
            children: {self.children if self.children else 'no children'},
            props: {self.props if self.props else 'no props'}
        )"""

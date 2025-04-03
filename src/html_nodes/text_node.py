from enum import Enum

from .leaf_node import LeafNode


class TextType(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        return self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if isinstance(text_node, TextNode):
        match text_node.text_type:
            case TextType.NORMAL:
                return LeafNode(tag=None, value=text_node.text)
            case TextType.BOLD:
                return LeafNode(tag="strong", value=text_node.text)
            case TextType.ITALIC:
                return LeafNode(tag="em", value=text_node.text)
            case TextType.CODE:
                return LeafNode(tag="code", value=text_node.text)
            case TextType.LINK:
                return LeafNode(
                    tag="a",
                    value=text_node.text,
                    props={"href": f"{text_node.url}"}
                )
            case TextType.IMAGE:
                return LeafNode(
                    tag="img",
                    value="",
                    props={
                        "src": text_node.url,
                        "alt": text_node.text
                    }
                )
            case _:
                raise ValueError("Not a valid text type")
    else:
        raise TypeError("Incorrect node type")

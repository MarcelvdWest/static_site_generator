from enum import Enum

from .leaf_node import LeafNode


class TextType(Enum):
    TEXT = "TEXT"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode():
    def __init__(self, text: str, text_type: TextType, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node: "TextNode"):
        return self.text == other_node.text and self.text_type == other_node.text_type and self.url == other_node.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    if isinstance(text_node, TextNode):
        match text_node.text_type:
            case TextType.TEXT:
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


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            raise TypeError("incorrect text type")

        # first_delimiter = node.text.find(delimiter)
        # last_delimiter = node.text.rfind(delimiter)

        # print(f"{first_delimiter=} {last_delimiter=}")

        seperate_string = node.text.split(delimiter)
        # print(seperate_string)

        new_nodes.extend(
            [
                TextNode(text=seperate_string[0], text_type=TextType.TEXT),
                TextNode(text=seperate_string[1], text_type=text_type),
                TextNode(text=seperate_string[2], text_type=TextType.TEXT)
            ]
        )

    return new_nodes

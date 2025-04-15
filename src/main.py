from html_nodes.text_node import TextNode, TextType, split_nodes_delimiter
from html_nodes.html_node import HTMLNode
from html_nodes.leaf_node import LeafNode
from html_nodes.parent_node import ParentNode


def main():
    print(TextNode("Test", TextType.BOLD, "https://www.google.com"))
    # print(TextNode("Test", TextType.BOLD, "https://www.google.com")).__repr__()
    # print(HTMLNode(None, None, None, None)).__repr__()
    # print(LeafNode(None, None, None).to_html())
    # print(LeafNode("Test", "p", None).to_html())
    # print(ParentNode("h2", [LeafNode("Test", "p", None)]).to_html())
    # print(
    #     ParentNode(
    #         "h2",
    #         [
    #             ParentNode("p", [LeafNode("Test", "strong", None)]),
    #             LeafNode("Test2", "p", {"class": "class-value"})
    #         ]
    #     ).to_html()
    # )
    # print(
    #     split_nodes_delimiter(
    #         [
    #             TextNode(
    #                 "This is text with a `code block` word",
    #                 TextType.TEXT
    #             )
    #         ],
    #         "`",
    #         TextType.CODE
    #     )
    # )


if __name__ == "__main__":
    main()

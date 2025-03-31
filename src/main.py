from html_nodes.text_node import TextNode, TextType
from html_nodes.html_node import HTMLNode
from html_nodes.leaf_node import LeafNode


def main():
    # print(TextNode("Test", TextType.BOLD, "https://www.google.com")).__repr__()
    # print(HTMLNode(None, None, None, None)).__repr__()
    # print(LeafNode(None, None, None).to_html())
    print(LeafNode("Test", "p", None).to_html())


if __name__ == "__main__":
    main()

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement to_html")

    def props_to_html(self):
        if not self.props:
            return ""
        return "".join([f' {key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        # Force children to be None for LeafNode
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value to render")

        if self.tag is None:
            return self.value  # raw text

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Cannot render ParentNode without a tag")
        if self.children is None:
            raise ValueError("Cannot render ParentNode without children")
        for child in self.children:
            print(f"Child type: {type(child)}, repr: {repr(child)}")

        inner_html = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>"

if __name__ == "__main__":
    child1 = LeafNode("b", "Bold text")
    child2 = LeafNode("i", "Italic text")
    parent = ParentNode("div", children=[child1, child2], props={"class": "container"})
    print(parent.to_html())


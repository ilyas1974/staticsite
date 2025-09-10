from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value=value, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            return self.value
        props_str = ''
        if self.props:
            props_str = ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"

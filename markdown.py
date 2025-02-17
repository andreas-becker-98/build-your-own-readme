

# Elements

class MarkdownDocumentElement:
    pass


class MarkdownTitle(MarkdownDocumentElement):
    def __init__(self, title: str) -> None:
        self.content = title
    
    def __str__(self) -> str:
        return f"# {self.content}"


class MarkdownDocument:
    def __init__(self) -> None:
        self.title = "Markdown Document"
        self.elements: list[tuple[str, str]] = []
    
    def set_title(self, title: str) -> None:
        self.title = title

    def add_section(self, header: str, content: str):
        self.elements.append((header, content))

    def __str__(self) -> str:
        element_strings = [f"# {self.title}"] + list(map(lambda elem: f"## {elem[0]}\n{elem[1]}", self.elements))
        return "\n\n".join(element_strings)


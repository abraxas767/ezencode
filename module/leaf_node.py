class LeafNode:

    parent: object = None
    child0: object = None
    child1: object = None
    code: int = None
    content: any = None

    def __init__(self, child0: object, child1: object, code: int, content: any):
        self.child0 = child0
        self.child1 = child1
        self.code = code
        self.content = content

    def is_numeric(self) -> bool:
        return str.isnumeric(self.content)

    def set_parent(self, parent: object) -> None:
        self.parent = parent


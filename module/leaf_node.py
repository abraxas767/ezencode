class LeafNode:

    parent: object = None
    child0: object = None
    child1: object = None
    code: int = None
    content: any = None
    prob: int = None
    is_numeric = False

    def __str__ (self):
        return "[content: {}, prob: {}, numeric: {}]".format(self.content, self.prob, self.is_numeric)

    def __init__(self, content: any, prob: int, is_numeric: bool):
        self.content = content
        self.prob = prob
        self.is_numeric = is_numeric

    def set_parent(self, parent: object) -> None:
        self.parent = parent

    def set_children(self, child0, child1):
        self.child0 = child0
        self.child1 = child1

    def set_code(self, code: int):
        self.code = code

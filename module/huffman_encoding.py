from leaf_node import LeafNode

class Huffman:

    EXAMPLE_STRING: str = "This is the huffman encoding"

    leafs = [] 
    prefix_table = {}

    def __init__(self):
        res = self.encode(self.EXAMPLE_STRING)
        dec = self.decode(res)

    def encode(self, data: str):
        freq = self.map_frequencies(data)
        sorted_freq = self.sort_frequencies(freq) 
        self.pair_frequencies(sorted_freq)
        self.create_prefix_table()

        res = ""
        for char in data:
            res += self.prefix_table[char]
        return res

    def decode(self, data: str):
        reverse_table = {val: key for key, val in self.prefix_table.items()} 
        res = ""
        tmp = ""
        for i in data:
            tmp += i
            if tmp in reverse_table:
                res += reverse_table[tmp]
                tmp = ""
        return res

    def create_prefix_table(self):
        self.add_to_prefix_table(self.leafs[0])

    def add_to_prefix_table(self, node):
        if not node.is_numeric:
            code = ""
            code += str(node.code)
            cursor = node
            while cursor.parent is not None:
                cursor = cursor.parent
                if cursor.code is not None:
                    code += str(cursor.code)
            self.prefix_table[node.content] = code[::-1]
        if node.child0 is not None and node.child1 is not None:
            self.add_to_prefix_table(node.child0)
            self.add_to_prefix_table(node.child1)
    
    def pair_frequencies(self, data: dict):
        if len(data) % 2 != 0:
            fill_node = LeafNode("xx", 0, False)
            self.leafs.append(fill_node)
        for i in data.items():
            leaf_node = LeafNode(i[0], i[1], False)
            self.leafs.append(leaf_node)
        self.gen_pairs(self.leafs)

    def gen_pairs(self, data):
        pairs = []
        while len(data) > 0:
            l1 = data[-1]
            del data[-1]
            l2 = data[-1]
            del data[-1]
            pair = LeafNode(l1.content + l2.content, l1.prob + l2.prob, True)
            pair.set_children(l1, l2)
            l1.set_parent(pair)
            l1.set_code(0)
            l2.set_parent(pair)
            l2.set_code(1)
            if len(data) == 1:
                pairs.append(data[0])
                del data[0]
            pairs.append(pair)
        
        pairs.sort(key=lambda x: x.prob, reverse=True)
        if len(pairs) == 1:
            self.leafs = pairs
            return 
        self.gen_pairs(pairs)
       
    def sort_frequencies(self, data: dict) -> dict:
        res = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
        return res

    def map_frequencies(self, data: str) -> dict:
        res = {i : data.count(i) for i in set(data)}
        return res

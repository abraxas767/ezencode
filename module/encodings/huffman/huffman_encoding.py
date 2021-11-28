from leaf_node import LeafNode
import sys
sys.path.insert(0, "./encodings/")
from abstract_encoding import Encoding

class HuffmanEncoding(Encoding):
    """ 
        This is the implementation of the huffman encoding.
    """

    __leafs = [] 
    __prefix_table = {}

    # generate prefix table and encode accordingly 
    def encode(self, data: str) -> str:
        # TODO save the generated prefix table and 
        # append it to the compressed result
        if data == '':
            raise ValueError('input cant be empty')
        self.__prefix_table = {}
        self.__leafs = []
        freq = self.__map_frequencies(data)
        sorted_freq = self.__sort_frequencies(freq) 
        self.__pair_frequencies(sorted_freq)
        self.__create_prefix_table()

        res = ""
        for char in data:
            res += self.__prefix_table[char]
        return res
    
    # receives input data and decodes with help of given prefix table
    def decode(self, data: str) -> str:
        # TODO Get the prefix table from input
        # and decode accordingly

        # reverse the table to be able to access prefixes as keys
        reverse_table = {val: key for key, val in self.__prefix_table.items()} 
        res = ""
        tmp = ""
        for i in data:
            tmp += i
            if tmp in reverse_table:
                res += reverse_table[tmp]
                tmp = ""
        return res

    # nudge recursive tree generation
    def __create_prefix_table(self) -> None:
        self.__add_to_prefix_table(self.__leafs[0])
    
    # generate prefix table entries recursivly
    def __add_to_prefix_table(self, node: object) -> None:
        if not node.is_numeric:
            code = ""
            code += str(node.code)
            cursor = node
            while cursor.parent is not None:
                cursor = cursor.parent
                if cursor.code is not None:
                    code += str(cursor.code)
            self.__prefix_table[node.content] = code[::-1]
        if node.child0 is not None and node.child1 is not None:
            self.__add_to_prefix_table(node.child0)
            self.__add_to_prefix_table(node.child1)
   
    # create leaf nodes
    def __pair_frequencies(self, data: dict) -> None:
        # check if odd
        if len(data) % 2 != 0:
            # create a fill node
            fill_node = LeafNode("xx", 0, False)
            self.__leafs.append(fill_node)
        for i in data.items():
            leaf_node = LeafNode(i[0], i[1], False)
            self.__leafs.append(leaf_node)
        self.__gen_pairs(self.__leafs)

    # recursive tree generation
    def __gen_pairs(self, data: list) -> None:
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
            self.__leafs = pairs
            return 
        self.__gen_pairs(pairs)
    
    # sort given frequencies alphabetically and according to probability 
    def __sort_frequencies(self, data: dict) -> dict:
        res = {k: v for k, v in sorted(data.items(), key=lambda item: (item[1], item[0]))}
        return res

    # map characters to frequencies
    def __map_frequencies(self, data: str) -> dict:
        res = {i : data.count(i) for i in set(data)}
        return res

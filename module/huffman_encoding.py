from collections import OrderedDict
from leaf_node import LeafNode

def pprint(d):
    if type(d) == dict:
        for s in d.items():
            print(s)
    elif type(d) == list: 
        for s in d:
            print(s)


class Huffman:

    EXAMPLE_STRING: str = "hello world1"

    def __init__(self):

        freq = self.map_frequencies(self.EXAMPLE_STRING)
        sorted_freq = self.sort_frequencies(freq) 
        groups = self.group_frequencies(sorted_freq)
        paired_freq = self.pair_frequencies(groups)
        nodes = self.generate_nodes(sorted_freq, paired_freq)
        tree = self.create_huffman_tree(paired_freq, nodes)
        self.create_prefix_table(tree)

    def create_prefix_table(self, huffman_tree):
        print(huffman_tree[0].is_numeric)


    def generate_nodes(self, sorted_freq, paired_freq):
        nodes = {}
        for key, val in sorted_freq.items():
            leaf = LeafNode(key, val, False)
            l = {key : leaf}
            nodes.update(l)
        if "xx" in paired_freq:
            nodes.update({ 0 : LeafNode("xx", 0, False)})
        pprint(nodes)
        print("\n")
        pprint(sorted_freq)
        return nodes

    def create_huffman_tree(self, paired_freq, nodes):
        huffman_tree = [] 
        for v in paired_freq.items():
            for pair in v[1]:
                first_leaf = nodes[pair[0]]
                sec_leaf = nodes[pair[1]]
                first_leaf.set_code(0)
                sec_leaf.set_code(1)

                prob = first_leaf.prob + sec_leaf.prob
                n = LeafNode(first_leaf.content + sec_leaf.content, prob, True)
                n.set_children(first_leaf, sec_leaf)

                first_leaf.set_parent(n)
                sec_leaf.set_parent(n)
                huffman_tree.append(n)

        while len(huffman_tree) > 1:
            layer = []
            count = 0
            while count < len(huffman_tree) -1 :
                first = huffman_tree[count]
                sec = huffman_tree[count + 1]
                prob = first.prob + sec.prob
                l = LeafNode(first.content + sec.content, prob, True)
                layer.append(l)
                count += 2
            if count == len(huffman_tree)-1:
                layer.append(LeafNode(huffman_tree[count].content, huffman_tree[count].prob, True))
            huffman_tree = layer
        return huffman_tree
    

    def pair_frequencies(self, data: dict):
        paired = {}
        left_over = None
        for group in data.items():
            # check if there was a leftover from previous cycle
            if left_over is not None:
                # if there is a leftover -> attach it at the end of group array
                group[1].append(left_over)
                left_over = None
            # check if group contains odd amount of items
            if len(group[1]) % 2 != 0:                 
                if group[0] == list(data)[-1]:
                    # append filling leaf node
                    group[1].append("xx")
                else:
                    # if odd -> declare first item a leftover
                    left_over = group[1][0]
                    del group[1][0]
            # pair items in groups
            leaf_node = { group[0] : list(self.chunks(group[1], 2)) }
            paired.update(leaf_node)
        return paired

    def chunks(self, lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n] 
        
    def group_frequencies(self, data: dict) -> dict:
        groups = {}
        for char, val in data.items():
            if not val in groups:
                groups[val] = [char]
            else:
                groups[val].append(char)
        return groups

    def sort_frequencies(self, data: dict) -> dict:
        res = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
        return res

    def map_frequencies(self, data: str) -> dict:
        res = {i : data.count(i) for i in set(data)}
        return res

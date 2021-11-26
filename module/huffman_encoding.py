from collections import OrderedDict

class Huffman:

    EXAMPLE_STRING: str = "This üis the huffman code implementation... and i dont know what else to say..."

    def __init__(self):
        freq = self.map_frequencies(self.EXAMPLE_STRING)
        sorted_freq = self.sort_frequencies(freq) 
        groups = self.group_frequencies(sorted_freq)
        self.huffman_tree(groups)

    def huffman_tree(self, data: dict):
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
            # leaf_node = { group[0] : list(self.chunks(group[1], 2)) }
        for i in data.items():
            print(i)

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

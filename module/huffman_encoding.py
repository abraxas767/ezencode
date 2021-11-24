from collections import OrderedDict

class Huffman:

    EXAMPLE_STRING: str = "This is the huffman code implementation..."

    def __init__(self):
        freq = self.map_frequencies(self.EXAMPLE_STRING)
        sorted_freq = self.sort_frequencies(freq) 
        groups = self.group_frequencies(sorted_freq)

        left_over = None
        for group in groups.items():
            # check if there was a leftover from previous cycle
            if not left_over == None:
                # if there is a leftover -> attach it at the end of group array
                group[1].append(left_over)

            # check if group contains odd amount of items
            if not len(group[1]) % 2 == 0:
                # if odd -> declare first item a leftover
                left_over = group[1][0]
                del group[1][0]
            print(group)
                
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

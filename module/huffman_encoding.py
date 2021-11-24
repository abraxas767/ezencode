from collections import OrderedDict

class Huffman:

    EXAMPLE_STRING: str = "This is the huffman code implementation..."

    def __init__(self):
        freq = self.map_frequencies(self.EXAMPLE_STRING)
        sorted_freq = self.sort_frequencies(freq)

    def sort_frequencies(self, data: dict) -> dict:
        res = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
        return res 

    def map_frequencies(self, data: str) -> dict:
        res = {i : data.count(i) for i in set(data)}
        return res

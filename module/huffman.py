class Huffman:

    EXAMPLE_STRING: str = "This is the huffman code implementation..."

    def __init__(self):
        frequencies = self.map_frequencies(self.EXAMPLE_STRING)
        for f, key in frequencies.items():
            print("{} --> {}".format(f, key))

    def map_frequencies(self, data):
        res = {i : data.count(i) for i in set(data)}
        return res

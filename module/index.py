import sys
sys.path.insert(0, "./encodings/huffman/")
from huffman_encoding import HuffmanEncoding
sys.path.insert(0, "./encodings/morse/")
from morse_encoding import MorseEncoding


def ask():
    print("Do you want to use [confirm with ENTER]")
    print("> encryption Huffman (1)")
    print("> encryption Morse (2)")
    i = input()
    return int(i)

def main()->None:
    huffman = HuffmanEncoding()
    morse = MorseEncoding()

    i = 0 
    try:
        while i not in range(1,3):
            try:
                i = ask()
            except ValueError:
                print("only numbers allowed")
                continue

        print("\nPlease enter your input: ")
        data = str(input())

    except KeyboardInterrupt:
        print("\n")
        sys.exit()

    
    try:
        if i == 1:
            res = huffman.encode(data)
            print("Encoded:\n->", res)
            print("Test decode:\n->", huffman.decode(res))

        elif i == 2:
            res = morse.encode(data)
            print("Encoded:\n->", res)
            print("Test decode:\n->", morse.decode(res))

    except ValueError as e:
        print(e)
        sys.exit()

if __name__ == "__main__":
    main()

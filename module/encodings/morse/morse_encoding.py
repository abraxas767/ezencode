import sys
sys.path.insert(0, "./encodings/")
from abstract_encoding import Encoding

class MorseEncoding(Encoding):
    """
        This is an experimental implementation of 
        morse encoding.
    """
   
    # morse alphabet
    prefix_table = {
        'A':'01','B':'1000','C':'1010','D':'100','E':'0',
        'F':'0010','G':'110','H':'0000','I':'00','J':'0111',
        'K':'101','L':'0100','M':'11','N':'10','O':'111',
        'P':'0110','Q':'1101','R':'010','S':'000','T':'1',
        'U':'001','V':'0001','W':'011','X':'1001','Y':'1011',
        'Z':'1100', ' ':'00000'}

    # encode given data according to prefix table
    def encode(self, data:str) -> str:
        if data == '':
            raise ValueError('input cant be empty')
    
        # convert lower case letters to uppercase
        data = data.upper()
        if not self.validate(data):
            raise ValueError("""Input includes characters not defined in morse.""")

        res = ""
        for char in data:
            res += self.prefix_table[char] + " "
        return res

    # decode given morse code according to prefix table
    def decode(self, data:str) -> str: 
        reverse_table = {val: key for key, val in self.prefix_table.items()} 
        res = ""
        tmp = ""
        for i in data:
            if i == " ":
                res += reverse_table[tmp]
                tmp = ""
            else:
                tmp += i
        return res

    # validate the input before continueing
    def validate(self, data: str) -> bool:
        for char in data:
            if not char in self.prefix_table:
                return False
        return True

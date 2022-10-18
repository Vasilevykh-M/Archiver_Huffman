class decompression:
    def __init__(self, FileNameInput = "", FileNameOtput = "",  root=None):
        self.FileNameInput = FileNameInput
        self.FileNameOutput = FileNameOtput
        self.root = root

    def dec_to_bin(self, num):
        rez = str(bin(num))[2:]
        while len(rez)!=8:
            rez = '0'+rez
        return rez

    def decompres(self):
        with open(self.FileNameInput, 'rb') as fileInput, open(self.FileNameOutput, 'w', encoding='utf-16') as fileOutput:
            symbol = fileInput.read(1)
            while symbol != b'':
                cur_Node = self.root
                code = self.dec_to_bin(symbol[0])

                while cur_Node.L or cur_Node.R:

                    if len(code) == 0:
                        symbol = fileInput.read(1)
                        code = self.dec_to_bin(symbol[0])

                    if code[0]=='0':
                        cur_Node=cur_Node.L
                    else:
                        cur_Node=cur_Node.R

                    code = code[1:]

                fileOutput.write(cur_Node.symbol)
                symbol = fileInput.read(1)
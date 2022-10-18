class compression:
    def __init__(self, FileNameInput = "", FileNameOtput = "",  dict ={}):
        self.FileNameInput = FileNameInput
        self.FileNameOutput = FileNameOtput
        self.dict = dict

    def compres(self):
        with open(self.FileNameInput, encoding="utf-16") as fileInput, open(self.FileNameOutput, 'wb') as fileOutput:
            symbol = fileInput.read(1)
            while symbol != '':
                fileOutput.write(self.dict[symbol])
                symbol = fileInput.read(1)
            fileOutput.write(self.dict[''])
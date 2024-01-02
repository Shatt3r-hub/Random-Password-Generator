import string
import random
import re


class Password:
    def __init__(self, charset, length):
        self.charset = charset
        self.length = length
        self.chararray = []
        self.password = ''

    def set_chararray(self):
        if(re.findall('[^ludsLUDS]+', self.charset)):
            print("\nInvalid charset provided !!\tSupported charset are 'lLuUdDsS' only\n")
            return(0);
        else:
            if('l' in self.charset or 'L' in self.charset):
                self.chararray.append(string.ascii_lowercase)
            if('u' in self.charset or 'U' in self.charset):
                self.chararray.append(string.ascii_uppercase)
            if('d' in self.charset or 'D' in self.charset):
                self.chararray.append(string.digits)
            if('s' in self.charset or 'S' in self.charset):
                self.chararray.append(string.punctuation)
        

    def pass_generator(self):
        for i in range(self.length):
            outer_index = random.randint(0, len(self.chararray)-1)
            inner_index = random.randint(0, len(self.chararray[outer_index])-1)
            self.password = self.password + self.chararray[outer_index][inner_index]
        return(self.password)

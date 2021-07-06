#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import os

starting_letter = "Input/Letters/starting_letter.txt"
invited_names = "Input/Names/invited_names.txt"
outDir = "Output/ReadyToSend/"

class Letter:
    def __init__(self, template, names):
        self.template = template
        self.names = names

    def openTemplateLetter(self, template):
        with open(template) as f:
            letter_text = f.read()
            return letter_text

    def listNames(self, names):
        with open(names)as n:
            return n.readlines()

    def replaceAll(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i,j)
        return text   


    def createLetters(self): 
        let = []
        text = self.openTemplateLetter(self.template)
        for name in self.listNames(self.names):
            #a = text.replace("[name]", name[:-1])
            d = {"[name]": name[:-1], "Angela":"Felipe"}
            a = self.replaceAll(text, d)
            with open(outDir+"letter_to_{}.txt".format(name[:-1]),"w") as l:
                l.write(a)

            




letter1 = Letter(starting_letter, invited_names) 
letter1.createLetters()


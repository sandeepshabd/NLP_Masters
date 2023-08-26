# tokenizer.py

import re

# Tokenizes a string. Takes a string (a sentence), splits out punctuation and contractions, and returns a list of
# strings, with each string being a token.

def readFileAndToeknize():
    wordCounter = {}

    string = readFile()
    stringArray = tokenize(string)
    for word in stringArray:
        if(word in  wordCounter):
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1
            
    for key in  wordCounter:
        if(wordCounter[key] >5):
            print(key+":"+str(wordCounter[key]))      
    
    
    
def readFile():
    f = open("/Users/sandeepshabd/Documents/study/austin/NLP/a0-distrib/NLP_Masters/week1/nyt.txt", "r")
    string = f.read()
    f.close()  
    return string
    
def tokenize(string):
    # print(repr(string))
    string = re.sub(r"[^A-Za-z0-9(),.!?\'`\-\"]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r"\.", " . ", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\?", " ? ", string)
    string = re.sub(r"\(", " ( ", string)
    string = re.sub(r"\)", " ) ", string)
    string = re.sub(r"\-", " - ", string)
    string = re.sub(r"\"", " \" ", string)
    # We may have introduced double spaces, so collapse these down
    string = re.sub(r"\s{2,}", " ", string)
    return list(filter(lambda x: len(x) > 0, string.split(" ")))

if __name__=="__main__":
   readFileAndToeknize()
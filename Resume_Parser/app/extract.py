from nltk.corpus import wordnet
import re
import os
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')

def extractemail(s):
    e = re.search('([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})', s)
    if e:
        print("hello")
        found = e.group(0)
        return found

def extractname(s):

    String=s
    Sentences = nltk.sent_tokenize(String)
    Tokens = []
    for Sent in Sentences:
        Tokens.append(nltk.word_tokenize(Sent))
    Words_List = [nltk.pos_tag(Token) for Token in Tokens]

    Nouns_List = []

    for List in Words_List:
        for Word in List:
            if re.match('[NN.*]', Word[1]):
                Nouns_List.append(Word[0])

    Names = []
    for Nouns in Nouns_List:
        if not wordnet.synsets(Nouns):
            Names.append(Nouns)

    return Names[0]
       

def extractphone(s):
    m = re.search(
        '((?:\+?\d{1,3}[\s-])?\(?\d{2,3}\)?[\s.-]?\d{3}[\s.-]\d{4,5})', s)
    if m:
        print("hello")
        found = m.group(0)
        return found
    else:
        phone=re.findall(re.compile(
            r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), s)

        if phone:
            number = ''.join(phone[0])
            if len(number) > 10:
                return '+' + number
            else:
                return number



def extractlinkedin (s):
    l = re.search('http(s)?:\/\/([\w]+\.)?linkedin\.com\/in\/[A-z0-9_-]*', s)
    if l:
        print("hello")
        found = l.group(0)
        return found


def extractlinesandchar (path_to_file):
    #FileTXT = 'C:/Users/admin/Desktop/ParseIT - Resume Parser/Resume_Parser/media/textfiles'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parentdir = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    mediadir = os.path.join(BASE_DIR, "media")
    txtdir = os.path.join(mediadir, "textfiles")

    base = os.path.basename(path_to_file)
    fileNAME = os.path.splitext(base)[0]
    fileTXT = fileNAME+'.txt'
    fileTXT = txtdir+'/'+fileNAME+'.txt'
    
    #filetxtpath = os.path.join(txtdir, fileTXT)
    #------------
    #base = os.path.basename(path_to_file)
    #fileNAME = os.path.splitext(base)[0]
    # number of lines in a text file
    # Opening a file

    file = open(fileTXT, "r", encoding="utf-8")
    Counter = 0

    # Reading from file
    Content = file.read()
    #get the length of the data
    number_of_characters = len(Content)
    tc = number_of_characters
    CoList = Content.split("\n")

    for i in CoList:
        if i:
            Counter += 1
    t = Counter
    print("This is the number of lines in the file")
    print(Counter)

    return t, tc




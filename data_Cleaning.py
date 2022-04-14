####################################       Data Cleaning        ###########################################


####################################      Import Packages        #######################################

import re
import string
from nltk import LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

####################################    Creating Objects  & Predefinitions     #######################################

# Create Instance Objects

lancaster = LancasterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()

# Predefinitions

punctuations = "?:!.,;"
ChangeTenseSubstring = ["ing", "ed"]
stopwordsArray = set(stopwords.words("english"))
# Array for all stop words
stopwordsArrayString = ''.join(map(str, set(stopwords.words("english"))))

# print(stopwordsArray)


####################################     Function Definition            #######################################

 # Remove tweets and unicode need to add and cover to regex learn https://docs.python.org/3/howto/regex.html
def data_cleaning1(documents):
    documents_clean = []
    for d in documents:
        # print(type(d))
        #Remove All Newline,-,| Characters
        document_test = " ".join(d.split("\n"))
        document_test = " ".join(document_test.split("-"))
        document_test = document_test.replace("|", " ")
        # Remove Unicode
        document_test = re.sub(r'[^\x00-\x7F]+', ' ', document_test)
        # Remove Mentions
        document_test = re.sub(r'@\w+', ' ', document_test)
        # Lowercase the document
        document_test = document_test.lower()
        # Remove punctuations
        document_test = document_test.translate(str.maketrans(' ', ' ', string.punctuation))
        # Lowercase the numbers
        document_test = re.sub(r'[0-9]', ' ', document_test)
        # Remove the doubled space
        document_test = re.sub(r'\s{2,}', ' ', document_test)
        documents_clean.append(" ".join(document_test.split()))
    documents.clear()
    for document in documents_clean:
        documents.append(document.split(" "))
    return documents



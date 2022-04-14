
####################################               Indexing                            #######################################

####################################            Import Packages                        #######################################
import math

####################################      Creating Objects & Predefinitions             #######################################

InvertedIdx = {}
####################################           Function Definition                      #######################################

#Test data which is overWritten
AllWordsFile = [['word1', 'word2', 'word4','word1'],['word3', 'word2', 'word1','word2', 'word4'],['word1', 'word2', 'word4','word4', 'word2', 'word4'],['word3', 'word2', 'word4','word2', 'word4'],['word1', 'word2', 'word4','word4', 'word2', 'word4']]

def normalized_term_frequency(word, document):
    raw_frequency = document.count(word)
    if raw_frequency == 0:
        return 0
    return 1 + math.log(raw_frequency)

def doc_contains_word(word,AllDocuments):
    count = 0
    for words in AllDocuments:
        if word in words:
            count += 1
    return count

def Significance(word,doc,total,n_doc):
    weight = normalized_term_frequency(word,doc)*(1+math.log(total/n_doc))
    return round(weight,3)

def data_indexing(documents,links):

    AllWordsFile = documents

    for words in AllWordsFile:
        idx = AllWordsFile.index(words)
        for word in words:
            if word not in InvertedIdx.keys():
                word_significance = Significance(word,words,len(AllWordsFile),doc_contains_word(word,AllWordsFile))
                InvertedIdx[word] = {}
                InvertedIdx[word]['link'] = []
                InvertedIdx[word]['significance'] = []

                InvertedIdx[word]['link'] += [links[idx]]
                InvertedIdx[word]['significance'] +=[word_significance]
            elif links[idx] not in InvertedIdx[word]['link']:
                word_significance = Significance(word, words, len(AllWordsFile), doc_contains_word(word, AllWordsFile))
                InvertedIdx[word]['link'] += [links[idx]]
                InvertedIdx[word]['significance'] += [word_significance]

    return InvertedIdx

# def data_cleaning(documents):
#     documents = [document.split(" ") for document in documents]
#     for document in documents:
#         temp_document = []
#         for i in range(len(document)):
#
#             for ch in document[i]:
#                 if ch in punctuations:
#                     document[i] = document[i].replace(ch, '')
#
#             for j in range(len(ChangeTenseSubstring)):
#                 document[i] = document[i].replace(ChangeTenseSubstring[j], '') if document[i].endswith(
#                     ChangeTenseSubstring[j]) else document[i]
#             document[i] = str.lower(wordnet_lemmatizer.lemmatize(document[i]))
#
#             if not document[i] in stopwordsArrayString:
#                 temp_document.append(document[i])
#
#         print(temp_document)
#         document.clear()
#         document.extend(temp_document)
#
#     return documents

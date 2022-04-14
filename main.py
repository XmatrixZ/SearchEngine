# Had to Run To download packages

# import nltk
# nltk.download('wordnet')
# nltk.download('stopwords')

# Import Packages

import data_Cleaning
import web_Crawling
import data_Indexing
import time
# Practice Data

document_1 = "I love watching movies when it's cold outside\n"
document_2 = "Toy Story is the best\n *^^% animation movie ever, I love it!"
document_3 = "Watching horror movies alone at &night is really scary"
document_4 = "He loves to watch films filled with suspense and unexpected plot twists"
document_5 = "My mom loves | - | to watch movies. ##My dad hates movie $ @ ! \n \n theaters. My brothers like any kind of movie. And I haven't watched a single movie since I got into college"
documents = [document_1, document_2, document_3, document_4, document_5]

def printInvertedIdx(InvertedIdx):
    for key in InvertedIdx:
        print(key)
        print(InvertedIdx[key]['link'],end=" ")
        print(InvertedIdx[key]['significance'])


if __name__ == "__main__":

    total = 0

    start = time.time()
    temp,linksList = web_Crawling.web_crawling()
    for subdata in temp:
        print(subdata)
    print(f"The Number of Links are: {len(linksList)}")
    print("hi")
    print(linksList)
    documents.clear()
    documents = temp
    end = time.time()
    print()
    print(total)
    total += end - start
    print(f"Time taken by the function: {end-start}")

    start = time.time()
    documents = data_Cleaning.data_cleaning1(documents)
    end = time.time()
    for document in documents:
        print(document)
    total += end - start
    print(f"Time taken by the function Data Cleaning Function-1: {end-start}")
    print()
    print(documents)
    print(len(documents))
    start = time.time()
    dictionary = data_Indexing.data_indexing(documents,linksList)
    end = time.time()
    printInvertedIdx(dictionary)
    total += end-start
    print(f"Time taken by the function Data Cleaning Function-1: {end-start}")
    print(total)

    file = open('dictionarydata.txt',"w+")
    file.write("%s\n" % dictionary)
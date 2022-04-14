####################################      Web Crawling            #######################################


####################################      Import Packages            #######################################
import multiprocessing
import re
import string
import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

####################################      Creating Objects & Predefinitions           #######################################


s = requests.Session()

# total-->Number of Retries backoff_factor--> Delay between each retry status_forcelist--> No retries for the following errors
retries = Retry(total=5,
                backoff_factor=0.2,
                status_forcelist=[500, 502, 503, 504])
s.mount('http://', HTTPAdapter(max_retries=retries))

# Make a request to website( Seed)
rSeed = s.get('https://www.semrush.com/blog/most-visited-websites/')

# Create an object to parse the HTML format
soupLinks = BeautifulSoup(rSeed.content, 'html.parser')


# All tags that are not text tags
blackList = [
    '[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script', 'style', 'img', 'map',
    'picture', 'area', 'video', 'track', 'sub', 'sup', 'strike', 'source', 'audio', 'code', 'command',
    'embed', 'eventsource', 'nav', 'link', 'canvas', 'figure', 'iframe', 'noframe', 'br', 'hr'
]


####################################     Function Definition            #######################################

def getLink(linksList):  # Retrieve all  links from the seed and return it
    for link in soupLinks.find_all('a', attrs={'href': re.compile("^https://")}):
        if link['href'] not in linksList:
            linksList.append(link['href'])
    return linksList

# Extract data from links using Multiprocessing
def fetchLinkData(link):
    data = s.get(link)
    return data

def getDataLink(linksList):

    # multiprocessing.cpu_count()--> Finding the count threads/cores present in the pc
    # Pool Function divides the whatever work you want equal between your current threads
    poolLinks = Pool(multiprocessing.cpu_count())

    #Store the string data from each links
    documentsDataLinks = []
    updatedDataLinks = []
    count = 0

    # Attempting to fetch data when unable to get even after retries skiping getting data from webpage
    while True:
        try:
            rLinksData = poolLinks.map(fetchLinkData,linksList)
            poolLinks.close()
            poolLinks.join()
        except ConnectionError:
            continue
        break

    #Extracting all text data from the fetched Webpage data
    for i in range(len(rLinksData)):
        lineoutput = ""
        soupLinksData = BeautifulSoup(rLinksData[i].content, 'html.parser')
        for linksData in soupLinksData.find_all(text=True):
            if linksData.parent.name not in blackList:
                lineoutput += '{} '.format(linksData)
        lineoutput = " ".join(lineoutput.split())
        documentsDataLinks.append(lineoutput)
        # updatedDataLinks.append(linksList[count])
        # count += 1
    return documentsDataLinks, linksList

def web_crawling():
    linksList = []
    documentsDataLinks = []
    start = time.time()
    linksList = getLink(linksList)
    end = time.time()
    print(f"Time taken by the function to get all the links is : {end - start}")
    print(f"The Number of Links are: {len(linksList)}")
    # print(linksList)
    documentsDataLinks,updatedList = getDataLink(linksList)
    return documentsDataLinks,linksList



# def getDataLink(linksList):
#     documentsDataLinks = []
#     updatedDataLinks = []
#     count = 0
#     for i in range(len(linksList)):
#         while True:
#             try:
#                 rLinksData = s.get(linksList[i])
#                 lineoutput = ""
#                 soupLinksData = BeautifulSoup(rLinksData.content, 'html.parser')
#                 for linksData in soupLinksData.find_all(text=True):
#                     if linksData.parent.name not in blackList:
#                         lineoutput += '{} '.format(linksData)
#                 lineoutput = " ".join(lineoutput.split())
#                 documentsDataLinks.append(lineoutput)
#                 updatedDataLinks.append(linksList[count])
#                 count += 1
#             except ConnectionError:
#                 continue
#             break
#     return documentsDataLinks,updatedDataLinks

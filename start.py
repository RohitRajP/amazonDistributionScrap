# importing beautifulSoup
from bs4 import BeautifulSoup
# importing requests library
import requests
import clipboard

# contructing URL to ping to get the website to scrap data
url = "https://www.amazondistribution.in/search?size=2page=1&ref_=sr_nr_crf_department";

# sending http GET request to get the contents of the website
html_doc = requests.get(url)

# getting the reponse HTML content
htmlContent = html_doc.content

# print(htmlContent)
# clipboard.copy(str(htmlContent))

# converting the html content into beautifulSoup object
soup = BeautifulSoup(html_doc.content,'html.parser')

# print(soup)

# getting to the unorderedList containing the list of items
ulBody = soup.find("ul",{"id":"result-list"})

i=0

# looping through all listItems in unorderedList 
for listItem in ulBody.findAll("li"):
    i+=1

print(i)
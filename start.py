# importing beautifulSoup
from bs4 import BeautifulSoup
# importing requests library
import requests
import clipboard
import csv 

fields = ['Image URL', 'Item Name', 'MRP', 'Incl.GST','Margins'] 

csvDataRows = []

querySize = 100

# contructing URL to ping to get the website to scrap data
url = "https://www.amazondistribution.in/search?size="+str(querySize)+"&page=1&ref_=sr_nr_crf_department"

# sending http GET request to get the contents of the website
html_doc = requests.get(url)

# getting the reponse HTML content
htmlContent = html_doc.content

# print(htmlContent)
clipboard.copy(str(htmlContent))

# converting the html content into beautifulSoup object
soup = BeautifulSoup(html_doc.content,'html.parser')

# print(soup)

# getting to the unorderedList containing the list of items
ulBody = soup.find("ul",{"id":"result-list"})

i=0

# looping through all listItems in unorderedList 
listItems = ulBody.findAll("li",{"class":"result-row"})
while i<querySize:
    print(i)

    try:
        img = str(listItems[i].find("img").attrs.get("src"))
        title = str(listItems[i].find("h3",{"class":"a-size-medium ws-search-product-title a-text-bold"}).text)
        # mrp = str(listItems[i].find("span",{"class":"a-size-medium"}).text)
        # mrp.replace('₹','')
        [mrp,inclGST,margin] = listItems[i].findAll("span",{"class":"a-size-medium"})
        mrp = str(mrp.text).replace('₹','')
        inclGST = str(inclGST.text).replace('₹','')
        margin = str(margin.text).strip()
    except AttributeError:
        print("\n\n Attribute Error")
    except IndexError:
        print("\n\n Index Error")
    # print("\n Image: "+img)
    # print(" Title: "+title)
    # print(" MRP: "+costDetails[0].text)
    # print(" Inc.GST: "+costDetails[1].text)
    # print(" Margin: "+str(costDetails[2].text).strip())

    dataRow = []
    dataRow.append(img)
    dataRow.append(title)
    dataRow.append(mrp)
    dataRow.append(inclGST)
    dataRow.append(margin)
    csvDataRows.append(dataRow)
    #print(dataRow)

    i += 1

#print(csvDataRows)

# name of csv file 
filename = "records.csv"

# writing to csv file 
with open(filename, 'w', encoding='utf-8', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
      
    # writing the fields 
    csvwriter.writerow(fields) 
      
    # writing the data rows 
    csvwriter.writerows(csvDataRows)
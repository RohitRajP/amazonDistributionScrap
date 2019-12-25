# importing beautifulSoup to parse html
from bs4 import BeautifulSoup
# importing requests library to send and recieve GET requests
import requests
# importing csv to write data into a csv file
import csv 
# importing webDriver for selenium
from selenium import webdriver
# importing ChromeDriverManager to install and user Chrome WebDriver
from webdriver_manager.chrome import ChromeDriverManager


# function to get the number of items on the website catelog
def getItemCount():
    # status print
    print("\n Getting the number of items...")
    # contructing URL to quickly get the html containing the number of items
    url = "https://www.amazondistribution.in/search?size=1&page=1&ref_=sr_nr_crf_department"
    # sending GET request to URL
    html_doc = requests.get(url)
    # creating a beautifulSoup object to parse the recieved html
    bSoupObj = BeautifulSoup(html_doc.content,'html.parser')
    # returning the number of items by parsing the HTML
    return int(str(bSoupObj.find("div",{"class":"a-row top-bar"}).find("div",{"class":"a-column a-span6 a-text-left"}).text).replace("Showing 1 to 1 of ","").replace(" Results",""))

# function to ping and get HTML content from the website
def pingPage(itemCount):
    # status print
    print("\n Starting Chrome WebDriver and redirecting to desired page...")
    # contructing URL to ping to get the website to scrap data
    url = "https://www.amazondistribution.in/search?size="+str(itemCount)+"&page=1&ref_=sr_nr_crf_department"
    # initating instance of chrome webdriver
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # open URL to parse data from
    browser.get(url)
    # returning the page source code
    return browser.page_source

# function to write contents to file
def writeToFile(mainPageHTML):
    # creating instace of file to write to
    file = open("index.html","w")
    # writing data to the file
    file.write(str(mainPageHTML.encode("utf-8")))
    # closing file instance
    file.close()

# function to parse the mainContentHTML and return the extractd data as a collection of lists
def parseHTML(mainContentHTML):
    # status print
    print("\n Parsing function initiated...")
    # holds the compiled data to be inserted into the csv file
    csvDataRows = []
    # converting the html content into beautifulSoup object
    bSoup = BeautifulSoup(mainContentHTML,'html.parser')
    # getting all relevant listItems in unorderedList 
    listItems = bSoup.findAll("li",{"class":"result-row"})
    # looping through all listItems
    for listItem in listItems:
        # holds all details of each item
        itemRow = []
        # get the item image URL and appending it to the itemRow list
        itemRow.append(str(listItem.find("img").attrs.get("src")))
        # get the item title and appending it to itemRow list
        itemRow.append(str(listItem.find("h3",{"class":"a-size-medium ws-search-product-title a-text-bold"}).text))
        print(itemRow)
        # getting the item pricing details 
        [mrp,inclGST,margin] = listItem.findAll("span",{"class":"a-size-medium"})
        # removing ₹ from the price text and appending it to itemRow list
        itemRow.append(str(mrp.text).replace('₹',''))
        itemRow.append(str(inclGST.text).replace('₹',''))
        # removing the empty spaces in the margin text and appending it to itemRow list
        itemRow.append(str(margin.text).strip())
        # appending itemRow list to csvDataRows
        csvDataRows.append(itemRow)
    # returning the compiled collection of itemRow lists
    return csvDataRows

# function to write data into csv file
def writeToCSV(csvDataRows):
    # holds the column headers for the generated csv file
    csvFieldHeaders = ['Image URL', 'Item Name', 'MRP', 'Incl.GST','Margins'] 
    # status print
    print("\n CSV Writing function initiated...")
    # name of csv file 
    filename = "records.csv"
    # writing to csv file 
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        # writing the column headers
        csvwriter.writerow(csvFieldHeaders) 
        # writing the data rows 
        csvwriter.writerows(csvDataRows)

# program execution begins here
if __name__ == "__main__":

    
    # holds the compiled data to be inserted into the csv file
    csvDataRows = []

    # status print
    print("\n\n Initializing AmazonScrap Script...")
    # get the number of items currently on the website catelog
    itemCount = getItemCount()
    # status print
    print("\n Item count recieved: "+str(itemCount))
    
    print("\n Initating web scrapper module...")
    # pings and get HTML content from website
    mainPageHTML = pingPage(itemCount)
    # status print
    print("\n Webpage HTML content retrieved")
    
    print("\n Writing HTML to file...")
    # writing the retrieved HTML into file
    writeToFile(mainPageHTML)
    # status print
    print("\n HTML content written to file")

    # status print
    print("\n Starting up HTML parsing module...")
    # parses the HTML and returns the list of items as a collection
    csvDataRows = parseHTML(mainPageHTML)
    # status print
    print("\n HTML parsing and collection compilation complete")

    # stauts print
    print("\n Initiating csv dataWrite module")
    # writing the data into csv file
    writeToCSV(csvDataRows)
    # status print
    print("\n Data successfully written to the csv file")











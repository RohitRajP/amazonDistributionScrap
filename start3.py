import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import clipboard

# initating instance of chrome webdriver
browser = webdriver.Chrome(ChromeDriverManager().install())

# open URL to parse data from
browser.get("https://www.amazondistribution.in/search?size=5000page=1&ref_=sr_nr_crf_department")
# reload the page to get rid of that annoying popup
browser.get("https://www.amazondistribution.in/search?size=5000page=1&ref_=sr_nr_crf_department")

# script to scroll to the bottom of the current page, wait 3 seconds for the next batch of data to load, 
# then continue scrolling. It will continue to do this until the page stops loading new data.
# get the length of the current page and scrolling to it
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);return document.body.scrollHeight;")
# set control variable to false
match=False
# use control variable to initiate loop to iterate the scrolling action
while(match==False):
        # assign the previous length of page to a temporary variable
        lastCount = lenOfPage
        # sleep for 3 seconds (time for new content to load)
        time.sleep(3)
        # get the new new updated page length and scrolling to it
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);return document.body.scrollHeight;")
        # compare the previous and current page length to check if there are changed
        if lastCount==lenOfPage:
            # flip the control variable to end loop
            match=True

# now that the page is fully scrolled, grab the source code.
source_data = browser.page_source
# convert the source code into a beautifulSoup object to start parsing
bs_data = bs(source_data,'html.parser')




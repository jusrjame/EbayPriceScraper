import sys
import urllib2
from bs4 import BeautifulSoup

url = "http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Auction=1&_nkw="
sorting = "&_sop=1"

if len(sys.argv) >= 1:

    # list of command line arguments except for
    # the program name itself
    arguments = sys.argv[1:]

    for word in arguments:
        # site holds an open version of the website
        page = urllib2.urlopen(url + word + sorting)

        soup = BeautifulSoup(page, "html.parser")

        # print soup

        # finds all <span> tags
        tags = soup.find_all('span', 'bold')

        #iterate thorough all span tags and print out the
        #the price data for each gpu on the page.
        for tag in tags:
            print tag.get_text()

        # website holds a copy of the webpage contents
        # website = site.read()

        # f = open(word + ".html", "w")
        # f.write(website)
        # f.close

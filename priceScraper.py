
import sys
import urllib2
from bs4 import BeautifulSoup

if len(sys.argv) > 1:

    # list of command line arguments except for
    # the program itself
    arguments = sys.argv[1:]

    for item in arguments:

        url = "http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Auction=1&_nkw=" + item + "&_sop=1"

        # site holds an open version of the website
        page = urllib2.urlopen(url)

        soup = BeautifulSoup(page, "html.parser")

        # finds all span with class="bold" tags
        tags = soup.find_all('span', 'bold')

        prices_text = []
        number_of_prices = 10
        # get the first 5 prices on the webpage
        for i in range(0, number_of_prices):
            prices_text.append(tags[i].get_text())

        # drop the '$' and save prices as a list of floats
        prices_float = []
        for price in prices_text:
            print price
            p = price[1:].replace(',', '')
            prices_float.append(float(p))

        total = 0.0
        # add the top 5 prices together
        for price in prices_float:
            total += price

        # get the average price of the top 5
        average_price = total / number_of_prices

        print ("{}: {}".format(item, average_price))

else:
    print ("Enter an item")

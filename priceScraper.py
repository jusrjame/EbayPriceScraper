import sys
import webbrowser as wb
import urllib2

url = "http://www.ebay.com/sch/i.html?_from=R40&_sacat=0&LH_Auction=1&_nkw="
sorting = "&_sop=1"

if len(sys.argv) >= 1:

    # list of command line arguments except for
    # the program name itself
    arguments = sys.argv[1:]

    for word in arguments:
        # site holds an open version of the website
        site = urllib2.urlopen(url + word + sorting)

        # website holds a copy of the content of the webpage
        website = site.read()

        f = open(word + ".html", "w")
        f.write(website)
        f.close

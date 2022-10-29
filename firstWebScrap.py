from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
"""
This is mt first webscrapping program.
It will scrape the websites containing the call to project for FDDs.
"""

# List of websites to scrape
# --------------------------
# Federation Wallonie Bruxelles
url1="https://www.wallonie.be/fr/appels-a-projets"
# SPF Santé
url2="https://www.health.belgium.be/fr/recherche-contractuelle/appels-projets-ouverts"
# Culture.be
url3="https://www.culture.be/index.php?id=17500"
# Economie sociale et solidaire
url4="https://economiesociale.be/appels-a-projets"

# Enseignement.be
url7="http://enseignement.be/index.php?page=25785"


# ----------------- FUNCTIONS ----------------- #
# Function to open the website and read the html
def openwebsite(url):
    wbsite=request.urlopen(url)
    wbsitesoup=BeautifulSoup(wbsite, 'html5lib')
    print(wbsitesoup.title.string)
    return wbsitesoup


# %%%%%%%%%%%%%%  Federation Wallonie Bruxelles %%%%%%%%%%%%%%
#currentsoup=openwebsite(url1)
# Find the table containing the call to project
# Make a list of all the http links in the class "item-list" containing "appel" and print them

"""currentsoup.find_all(attrs={"class": "item-list"})
for link in currentsoup.find_all('a', href=re.compile("appel")):
    print(link.get('href'))
"""

# %%%%%%%%%%%%%%  SPF Santé %%%%%%%%%%%%%%
#currentsoup=openwebsite(url2)

# Find the h3 in the div named "middle"
"""currentsoup.find_all(attrs={"class": "middle"})
for h3 in currentsoup.find_all("h3"):
    print(h3.text)
    print(h3.find_next_sibling("h4").text)
"""

# %%%%%%%%%%%%%%  Culture.be %%%%%%%%%%%%%%
currentsoup=openwebsite(url3)
# Print span news-list-date, print h3, a href title, p, span news-list-morelink
for span in currentsoup.find_all(attrs={"class": "news-list-date"}):
    print(span.text)
    print(span.find_next_sibling("h3").text)
    print("https://www.culture.be/"+span.find_next_sibling("h3").find_next_sibling("a").get('href')+"")
    print(span.find_next_sibling("h3").find_next_sibling("a").get('title'))
    print(span.find_next_sibling("h3").find_next_sibling("p").text)
    print(span.find_next_sibling("h3").find_next_sibling("p").find_next_sibling(span.text))
    print("")



# %%%%%%%%%%%%%%  Economie sociale et solidaire %%%%%%%%%%%%%%
#currentsoup=openwebsite(url4)

# %%%%%%%%%%%%%%  Enseignement.be %%%%%%%%%%%%%%
#currentsoup=openwebsite(url7)



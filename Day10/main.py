from bs4 import BeautifulSoup as bs
import urllib.request
import csv

url = "https://www.iana.org/domains/reserved"
page = urllib.request.urlopen(url)

print(page)

#Cooking the Soup
soup = bs(page,"html.parser")
#
print(soup.title.string)
# print(soup.p)
rows = soup.find(id="arpa-table").find_all("tr")






import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['languages']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in rows:
        cols =row.find_all('td')
        if len(cols)>0:
             print(cols[2].string)
             writer.writerow({'languages': cols[2].string})

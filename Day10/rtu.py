from bs4 import BeautifulSoup as bs
import urllib.request
import csv

url = "http://www.espncricinfo.com/ci/engine/match/903605.html"
page = urllib.request.urlopen(url)

print(page)

#Cooking the Soup
soup = bs(page,"html.parser")
#
print(soup.title.string)
# print(soup.p)
rows = soup.find_all("div", class_="wrap batsmen")
for row in rows:
    print(row.prettify())





# import csv
#
# with open('rtu.csv', 'w') as csvfile:
#     fieldnames = ['sno','city','college','center']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     for row in rows:
#         cols =row.find_all('td')
#         if len(cols)>0:
#              print(cols[2].string)
#              writer.writerow({'sno': cols[0].string,'city': cols[1].string,'college': cols[2].string,'center': cols[3].string,})

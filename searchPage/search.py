import requests
from bs4 import BeautifulSoup

from urllib.request import urlopen

# Collect and parse first page
page = 'www'
soup = BeautifulSoup(page.text, 'html.parser')

#print(soup)
# Pull all text from the BodyText div
artist_name_list = soup.find(class_='profile-list')

#artist_name_list = soup.find_all(class_="profile-list")

#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.get_text())
#print (soup.title)
#print(artist_name_list)


url = 'www'
html = urlopen(url).read()
soup = BeautifulSoup(html)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text.encode('utf-8'))




# Pull text from all instances of <a> tag within BodyText div
#artist_name_list_items = artist_name_list.find_all('a')
#print(artist_name_list_items)

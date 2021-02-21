import requests
from bs4 import BeautifulSoup
import re
from datetime import date

#set date for file name later
today = date.today()
d4 = today.strftime("%b-%d-%Y")

#scrape website
url = "https://abnursepractitioners.nationbuilder.com/join_us"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
namelist = soup.find_all(class_='activity-oneliner')

#create list of donation event text
donations = []
for entry in namelist:
    donations.append(entry.text)

donations_clean = []
for item in donations:
    donations_clean.append(re.sub(r"[\n\t]*", "",item))  

#extract items with 'via'
via=[]
not_via=[]
for donat in donations_clean:
    if 'donated via' in donat:
        via.append(donat)
    else:
        not_via.append(donat)

with open('self_donated' + '-' + str(d4) + '.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(set(not_via)))

with open('donated_via' + '-' + str(d4) + '.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(set(via)))
    

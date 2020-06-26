from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
a = str(soup)
b = a.find('<li>Total')
c = b+59
print(a[b:c])
data = a[b:c]
f = open('data.json', 'w')
f.write('{')
f.write('\n')
f.write(data)
f.write('\n')
f.write('}')
f.close

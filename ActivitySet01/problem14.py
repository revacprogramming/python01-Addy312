# Using Web Services
# https://www.py4e.com/lessons/servces
# Beautiful soup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the url : ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


sum = 0
# Retrieve all of the span tags
tags = soup("span")
for tag in tags:
    # Look at the parts of a tag
    sum += int(tag.contents[0])

print(sum)
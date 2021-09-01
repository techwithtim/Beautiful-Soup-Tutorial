from bs4 import BeautifulSoup
import requests

# HTML From File
with open("index.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")

tags = doc.find_all("p")[0]

print(tags.find_all("b"))

# HTML From Website
url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

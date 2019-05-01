import urllib.request
import re

author = "Ian+Goodfellow"
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
find_pattern = 'title is-5 mathjax[\s\S]*?</p>'
result = re.findall(find_pattern, html_str)

print("[ Author: " + author + " ]")
for r in result:
	title=r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
	print(title)


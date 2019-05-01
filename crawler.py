import urllib.request
import re

author = "Ian+Goodfellow"
error = []
start = 0

print("[ Author: " + author + " ]")

while error == []:
	url = "https://arxiv.org/search/?searchtype=author&query=" + author + "&abstracts=hide&size=50&order=-announced_date_first&start=" + str(start)
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	find_warning = "Sorry, your query for"
	error = re.findall(find_warning, html_str)
	if error != [] :
		print("\n[end of list]")
	else:
		find_pattern = 'title is-5 mathjax[\s\S]*?</p>'
		result = re.findall(find_pattern, html_str)

		for r in result:
			title=r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
			print(title)

		start=start+50


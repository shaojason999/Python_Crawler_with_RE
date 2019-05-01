import urllib.request
import re
import matplotlib.pyplot as plt

author = "Ian+Goodfellow"
error = list()
start = 0
find_title = 'title is-5 mathjax[\s\S]*?</p>'
find_year = 'originally announced</span>[\s\S]*?</p>'
year_ans = list()
x = list()
y = list()
max_count = 0

print("[ Author: " + author + " ]")

while error == []:
	url = "https://arxiv.org/search/?searchtype=author&query=" + author + "&abstracts=hide&size=50&order=-announced_date_first&start=" + str(start)
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	find_warning = "Sorry, your query for"
	error = re.findall(find_warning, html_str)

	# stop crawling
	if error != [] :
		print("\n[end of list]")

		max_year=max(year_ans)
		max_year=int(max_year)
		min_year=min(year_ans)
		min_year=int(min_year)

		for i in range(min_year, max_year+1):
			count=year_ans.count(str(i))

			# in order to set the y-axis
			if count > max_count:
				max_count = count
			y.append(count)
			x.append(i)
		# set the y-axis
		plt.yticks(range(0,max_count+1,2))
		plt.bar(x,y)
		plt.show()
	else:
		# find the titles
		result = re.findall(find_title, html_str)

		for r in result:
			title=r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
			print(title)

		# find the originally announced years"
		result = re.findall(find_year, html_str)

		for r in result:
			date = r.split("</span>")[1].split("</p>")[0].strip()
			year = re.findall("[0-9]+", date)
			year_ans.append(year[0])


		start=start+50






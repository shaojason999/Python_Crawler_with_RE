import urllib.request
import re
import matplotlib.pyplot as plt

find_list = 'arxiv-result[\s\S]*?</li>'
find_author = '>[\s\S]*?</a>'

temp_author_list = list()
coauthor_list = list()
year_ans = list()
error = list()
x = list()
y = list()

max_count = 0
start = 0

author = input()
search_author=author.replace(' ','+')
print("[ Author: " + author + " ]")

while error == []:
	url = "https://arxiv.org/search/?searchtype=author&query=" + search_author \
		+ "&abstracts=hide&size=50&order=-announced_date_first&start=" + str(start)
	content = urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	find_warning = "Sorry, your query for"
	error = re.findall(find_warning, html_str)

	# stop crawling
	if error != [] and coauthor_list == []:
		print("no result")
	elif error != [] and coauthor_list != []:
		print("[ end of title list ]")

		# print coauthors
		print("\n[ Co-author list ]")
		coauthor_list.sort()
		
		while coauthor_list != []:
			count = coauthor_list.count(coauthor_list[0])
			print(coauthor_list[0] + ": %d times" %(count))
			del coauthor_list[0:count]

		print("[ end of coauthor list ]")

		# draw the bar chart
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
			x.append(str(i))
		# set the y-axis
		plt.yticks(range(0,max_count+1,2))
		plt.bar(x,y)
		plt.savefig("bar_chart.png")
#		plt.show()
	else:
		#find the result lists
		list_result = re.findall(find_list, html_str)
		for l_r in list_result:
			# find the coauthors
			temp_author_list.clear()
			authors = l_r.split("Authors:</span>")[1].split("</p>")[0].strip()
			each_author = re.findall(find_author, authors)
			for a_r in each_author:
				result = a_r.split(">")[1].split("</a")[0].strip()
				temp_author_list.append(result)

			# find if the author is in the coauthor list
			for temp_author in temp_author_list:
				if author.lower() == temp_author.lower():
					coauthor_list = coauthor_list + temp_author_list

					# find the titles
					title = l_r.split("title is-5 mathjax\">")[1].split("</p>")[0].strip()
					print(title)

					# find the originally announced years
					date = l_r.split("originally announced</span>")[1].split("</p>")[0].strip()
					year = re.findall("[0-9]+", date)
					year_ans.append(year[0])

					break;
		start=start+50


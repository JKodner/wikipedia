# citation book-news-web-journal-pressrelease-audio-visual-OTHER

def wiki(topic):
	import requests
	from BeautifulSoup import BeautifulSoup
	references = {
		"book": [],
		"news": [],
		"web": [],
		"journal": [],
		"other": []
	}
	url = "http://en.wikipedia.org/wiki/" + topic.replace(" ", "_")
	html = requests.get(url).text
	soup = BeautifulSoup(html)
	refs = soup.findAll("span", {"class":"reference-text"})
	for i in refs:
		if i.find("span", {"class":"citation book"}):
			references["book"].append(i.text)
		elif i.find("span", {"class":"citation news"}):
			references["news"].append(i.text)
		elif i.find("span", {"class":"citation web"}):
			references["web"].append(i.text)
		elif i.find("span", {"class":"citation journal"}):
			references["journal"].append(i.text)
		else:
			references["other"].append(i.text)
	return references
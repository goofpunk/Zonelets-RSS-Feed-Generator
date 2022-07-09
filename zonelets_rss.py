import re, datetime

blog_title = "goofpunk blog"
blog_link = "https://goofpunk.com/blog/"
blog_description = "The blog for goofpunk.com"

filenames = []
dates = []
articlenames = []
posts_dict = {}
xml_items = []

xml_format = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>""" + blog_title + """</title>
  <link>""" + blog_link +  """</link>
  <description>""" + blog_description + """</description>
REPLACETHIS
</channel>

</rss>"""

# split lines into the filename and the title
def splitPosts(inputFile):
	splitFile = inputFile.split(",")
	
	filenames.append(splitFile[0])
	dates.append(splitFile[0][9:19])
	articlenames.append(splitFile[1])

# create XML items
def createItemXLML(fName, aName, fDate):
	return """  <item>
    <title>""" + aName + """</title>
    <link>""" + blog_link + fName + """</link>
    <pubDate>""" + fDate + """</pubDate>
  </item>"""

# get raw text out of the JS file
with open('script.js') as infile:
	copy = False
	for line in infile:
		if line.strip() == "//POSTS_START":
			copy = True
			continue
		elif line.strip() == "//POSTS_END":
			copy = False
			continue
		elif copy:
			file = line.strip()
			splitPosts(file)

for i in range(0, len(filenames)):
	filename = filenames[i][3:-1]
	if i == len(filenames) - 1:
		articlename = articlenames[i][12:-7]
		print(articlename)
	else:
		articlename = articlenames[i][12:-5]
		print(articlename)
	
	formatted_date = datetime.datetime.strptime(dates[i], '%Y-%m-%d').strftime('%a, %d %b %Y 01:00:00 GMT')
	
	xml_items.append(createItemXLML(filename, articlename, formatted_date))
	

# combine XML items into a single string
joined_items = "\n"
joined_items = joined_items.join(xml_items)

final_file = re.sub("REPLACETHIS", joined_items, xml_format)

with open("rss.xml", "w") as o:
	o.write(final_file)
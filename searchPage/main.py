import re
from urllib.request import urlopen

for i in range(1, 200, 1):
	
	page = 'url'
	html_content = urlopen(page).read().decode('utf-8')

	#print(html_content)	
	print(page)
	matches = re.findall('texttofind', html_content);
	
	if len(matches) == 0:
   		print('I did not find anything' + " " + str(i))
	else:
   		print('My string is in the html')



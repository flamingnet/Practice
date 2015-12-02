import urllib2

response = urllib2.urlopen('http://gutenberg.org/files/135/135-h/135-h.htm#link2H_4_0347/')
html = response.read()

happy = 0

list_of_words = html.split(' ')

for word in list_of_words:
	if word == 'Les Miserables':
		happy += 1

print happy
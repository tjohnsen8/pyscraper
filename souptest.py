import requests
from bs4 import BeautifulSoup
import collections

ignore_words = ['that', 'there', 'the', 'and', 'i\'m']
ignore_words += ['from', 'she', 'you', 'him', 'his', 'her']
ignore_words += ['it\'s', 'i\'ll']

nono_words = ['fuck', 'shit', 'ass', 'bitch', 'cock', 'pussya', 'nigga']
nono_words += ['fucks', 'fucker', 'motherfucker', 'fucking', 'motherfucking']
nono_words += ['shitting', 'shittin', 'shits', 'shitter']
nono_words += ['asshole', 'asses', 'assholes']
nono_words += ['bitches', 'niggas']
nono_words += ['cocks', 'cocksucker']
nono_words += ['pussies', 'puss', 'pussed']

# r = requests.get("http://www.metrolyrics.com/alright-lyrics-kendrick-lamar.html")
r = requests.get("http://www.metrolyrics.com/the-heart-part-4-lyrics-kendrick-lamar.html")
data = r.text
soup = BeautifulSoup(data, "html5lib")

words = []
for p in soup.find_all(lambda tag: tag.name == 'p' and tag.get('class') == ['verse']):
	 for item in p.contents:
		if item.string != None:
			words.extend(item.string.encode('ascii','ignore').lower().split())
# want to remove the prounouns and 
# for words in collections.Counter(words).most_common(10):
#	print words
words = [word for word in words if word not in ignore_words and len(word) > 2]
bad_words = [word for word in words if word in nono_words]
# print [word for word in collections.Counter(words).most_common(10)]
print collections.Counter(words)
print collections.Counter(bad_words)

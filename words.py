import requests

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
WORDS_T = [str(n, 'utf-8') for n in WORDS]



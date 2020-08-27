# @Date:   2019-01-03T11:34:37+01:00
# @Last modified time: 2019-01-03T16:33:23+01:00

#return some info into http response
from django.http import HttpResponse
from django.shortcuts import render
import operator

#every time someone come visit the page it will send this request
def home(request):
	#request, redirect to home.html, with a dictionary
	return render(request, 'home.html')

def count(request):
	#this retrieve the text from the form fulltext
	fulltext = request.GET['fulltext']

	#every word is splited in one case
	wordlist = fulltext.split()

	worddictionary = {}
	#loop throug each word
	for word in wordlist:
		if word in worddictionary:
			#increase the dictionary
			worddictionary[word] += 1
		else:
			#add to the dictionary
			worddictionary[word] = 1

	sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	#					,				, I can use fulltext in count.html -> this will give me the value
	return render(request, 'count.html', {'fulltext':fulltext, 'countword':len(wordlist), 'sortedwords':sortedwords})



def goat(request):
	#send a HttpResponse with html code inside
	#return HttpResponse("<h1>THIS IS GOAT VILLAGE !</h1>")
	return render(request, 'goathome.html', {'Welcome':'THIS IS GOAT VILLAGE !'})

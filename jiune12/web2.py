import urllib.request
pageurl = urllib.request.urlopen("http://www.google.com")
print(str(pageurl.getcode()))

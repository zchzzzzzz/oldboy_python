import urllib
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getMovieName(html):
    reg = r'<img alt="(.+?)" src'
    MovieName = re.compile(reg)
    Namelist = re.findall(MovieName,html)
    return Namelist

i = 1
for n in range(1,11):
    m = 25*(n-1)
    html = getHtml("http://movie.douban.com/top250?start=%d&filter=" %m).decode('utf-8')
    for x in getMovieName(html):
        print('Top %3d: %s' %(i,x))
        i += 1
print ('finish!')
import urllib
import urllib.request
import re
def gethtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    return html
def getPassword(html):
    reg=""
    Password=re.compile(reg)
    PasswordList=re.findall(Password,html)
    return PasswordList
html1=gethtml("").decode("utf8")
i=1
for n in getPassword(html1):
    urllib.request.urlretrieve(n,"报错路径 /%s.txt" %i)
    print("%s/%s"%(i,len(getPassword(html1))))
    i+=1
    print("done")
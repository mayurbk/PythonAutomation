#BeautifulSoup is use to parse html (extracting html)
import bs4,requests
# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text,'html.parser')  #stores the entire html page as a beautifulsoup object
# print(type(noStarchSoup))

exmFile = open('example.html')  #keeping the 'example.html ' file in the working directory.
#exmplSoup = bs4.BeautifulSoup(exmFile,'html.parser')
#print(type(exmplSoup))

##Finding element with the Select() method
exmplhtml= bs4.BeautifulSoup(exmFile.read(),'html.parser')
values = exmplhtml.select('#author')   #values will be a list of tag objects
print(type(values))
print(len(values))
print(values)
str(values[0])
print(values[0].getText())

paraElements = exmplhtml.select('p')
print(type(paraElements))
print(paraElements)
str(paraElements[0])
print(paraElements[0].getText())
print(paraElements[1].getText())
print(paraElements[2].getText())

paraTitle = exmplhtml.select('title')
print(type(paraTitle))
print(paraTitle)
str(paraTitle[0])
print(paraTitle[0].getText())
#opening browser
# import webbrowser
# webbrowser.open('https://www.koenig-solutions.com/')

#download/extracting files through request module
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(res.status_code == requests.codes.ok)
print(len(res.text))
print(res.text[:300])
data = open('downloadFile.txt','wb') #write in binary size
for i in res.iter_content(10000):  ##chunk size is in bytes
    data.write(i)

data.close()
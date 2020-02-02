import requests
from bs4 import BeautifulSoup
class Crawler():
  def getData(self):
    page = requests.get("https://theinternship.io/")
    soup = BeautifulSoup(page.content, 'html.parser')
    logo_box = soup.find_all(class_='logo-box')
    desc = self.getDesc(soup)
    image_url = [item.find('img')['src'] for item in logo_box]
    data = []
    
    for num in range(len(image_url)):
      data.append({
        "url": image_url[num],
        "desc": desc[num]
      })
    return data

  def getDesc(self, soup):
    list_company = soup.find_all(class_='list-company')
    desc = [item.text for item in list_company]
    return desc
  
  def downloadImage(self, data):
    for item in data:
      img_data = requests.get("https://theinternship.io/" + item['url']).content
      with open("./" + item['url'], 'wb') as handler:
        handler.write(img_data)
    return True

  def saveUrl(self, data):
    file = open("url.txt", "w")
    for item in data:
      file.write(item["url"] + "\n")

  def __init__(self):
    data = self.getData()
    self.downloadImage(data)
    self.saveUrl(data)
    data_sort = sorted(data, key=lambda item: len(item['desc']))
    print("\n".join(list(map(lambda x: x['url'], data_sort))))
    
    # print([len(x['desc']) for x in data_sort]) # check length
    
if __name__ == "__main__":
    Crawler()
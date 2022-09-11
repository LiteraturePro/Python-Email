from leancloud import Engine
from leancloud import LeanEngineError
import leancloud
import requests
import uuid
from bs4 import BeautifulSoup
engine = Engine()

def download_img(url,path):
  try:
    respone = requests.get(url)
    f_img = respone.content
    with open(path, "wb")as f:
        f.write(f_img)
  except Exception as e:
    print("---------地址出错------------")

@engine.define
def get_infos(**params):
    if 'name' in params:

        return ''
    
    
    else:
        url = "http://www.wufazhuce.com/"
        page = requests.get(url).content
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page, 'html.parser')
        for i in soup.find_all('div',class_ = 'item'):
            onelist = i.find_all('a')
            image = onelist[0].img['src']
            word = onelist[1].text
            infolist = i.find_all('p')
            id = infolist[0].text
            date = infolist[1].text+' '+infolist[2].text
        list = []
        soup = BeautifulSoup(page, 'html.parser')
        for i in soup.find_all('div',class_ = 'item'):
            onelist = i.find_all('a')
            image = onelist[0].img['src']
            word = onelist[1].text
            infolist = i.find_all('p')
            id = infolist[0].text
            date = infolist[1].text+' '+infolist[2].text
            data = {
                'image':image,
                'word':word,
                'id':id,
                'date':date
                }
            list.append(data)
        # 声明 class
        Words = leancloud.Object.extend('word')

        # 构建对象
        words = Words()
        print(list[0]["word"])
        print(list[0]["image"])

        # 为属性赋值
        words.set('word', list[0]["word"])
        # 将对象保存到云端
        words.save()
        
        img_path  = str(uuid.uuid4())+'.png'
        
        download_img(list[0]["image"],'/tmp/'+img_path)
        
        with open(('/tmp/'+img_path, 'rb') as f:
            file = leancloud.File(img_path, f)
            file.key = img_path
            file.save()
        print(file.url)

        return list[0]["word"]

from leancloud import Engine
from leancloud import LeanEngineError
import leancloud
import requests
import uuid
from bs4 import BeautifulSoup
engine = Engine()


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
        
        file = leancloud.File.create_with_url(str(uuid.uuid4())+'.png', list[0]["image"])
        file.save()
        print(file.url)

        return list[0]["word"]

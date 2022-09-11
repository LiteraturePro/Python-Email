from leancloud import Engine
from leancloud import LeanEngineError
import leancloud

engine = Engine()

# 内容爬取
def get_info():
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
    return list[0]

@engine.define
def get_infos(**params):
    if 'name' in params:
        info = get_info().get("word")
        # 声明 class
        Words = leancloud.Object.extend('words')

        # 构建对象
        words = Words()

        # 为属性赋值
        words.set('word',   info)
        # 将对象保存到云端
        words.save()
        
        return 'info'
    
    
    else:
        return 'Hello, LeanCloud!'

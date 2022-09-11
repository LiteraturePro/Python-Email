from flask import Flask
from flask import Flask, jsonify, request
from flask import render_template
import os
import leancloud 
import datetime
import requests
leancloud.init(os.environ['LEANCLOUD_APP_ID'], master_key=os.environ['LEANCLOUD_APP_MASTER_KEY'])


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

#*************定义天气信息爬取函数*************#
def get_weather(url):

    #天气爬取
    try:
        r = requests.get(url, timeout = 30)       #用requests抓取网页信息
        r.raise_for_status()                      #可以让程序产生异常时停止程序
        r.encoding = r.apparent_encoding
        html=r.text
    except:
        html="err"
    final_list = []
    soup = BeautifulSoup(html,'html.parser')       #用BeautifulSoup库解析网页
    body  = soup.body
    data = body.find('div',{'id':'7d'})
    ul = data.find('ul')
    lis = ul.find_all('li')
    for day in lis:
        temp_list = []       
        date = day.find('h1').string             #找到日期
        temp_list.append(date)        
        info = day.find_all('p')                 #找到所有的p标签
        temp_list.append(info[0].string)   
        if info[1].find('span') is None:          #找到p标签中的第二个值'span'标签——最高温度
            temperature_highest = ' '             #用一个判断是否有最高温度
        else:
            temperature_highest = info[1].find('span').string
            temperature_highest = temperature_highest.replace('℃',' ')

        if info[1].find('i') is None:              #找到p标签中的第二个值'i'标签——最高温度
            temperature_lowest = ' '               #用一个判断是否有最低温度
        else:
            temperature_lowest = info[1].find('i').string
            temperature_lowest = temperature_lowest.replace('℃',' ')

        temp_list.append(temperature_highest)       #将最高气温添加到temp_list中
        temp_list.append(temperature_lowest)        #将最低气温添加到temp_list中

        wind_scale = info[2].find('i').string      #找到p标签的第三个值'i'标签——风级，添加到temp_list中
        temp_list.append(wind_scale)

        final_list.append(temp_list)              #将temp_list列表添加到final_list列表中


    # 当爬取完毕，进行邮件内容设置，生成html邮件
    return final_list[1]




app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api')
def api():
    lists = []
    users = leancloud.Object.extend('users')
    users_query = users.query
    users_list = users_query.find()
    for user in users_list:
        content = []
        content.append(user.get("address"))
        content.append(get_info().get("image"))
        content.append(get_info().get("word"))
        content.append(get_info().get("date"))
        content.append("http://leancloud.wxiou.cn/"+datetime.datetime.now().strftime('%Y-%m-%d')+".mp3")
        content.append(get_weather(user.get("city"))[0])
        content.append(get_weather(user.get("city"))[1])
        content.append(get_weather(user.get("city"))[2])
        content.append(get_weather(user.get("city"))[3])
        lists.append(content)
    return lists

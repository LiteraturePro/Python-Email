#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import random
import requests
import string
import datetime
import csv
import schedule
import time
import pymysql
import pandas as pd
from bs4 import BeautifulSoup
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText



#*************定义数据库使用全局字段*************#

user_name = 'literature'                                    #数据库用户名
password = 'yxl981204@'                                     #数据库密码
address = 'rm-2zefgw4028bthwjxgvo.mysql.rds.aliyuncs.com'   #数据库地址
port = 3306                                                 #数据库端口



#*************定义邮件全局字段*************#

mail_host="smtp.qq.com"           #设置代理服务器，QQ邮箱，网易邮箱等
mail_user="2440229611@qq.com"     #用户名
mail_pass="hczyrlhfykfwebhh"      #邮件口令




#*************定义辅助函数*************#
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


#*************定义邮件发送函数*************#
def send_mail(to_list,sub,content):                               #定义一个函数，收件人、标题、邮件内容
    me="test"+"<"+mail_user+">"                                   #发件人定义,这里要和认证帐号一致才行的
    msg = MIMEText(content,_subtype='html',_charset='utf-8')      #这里看email模块的说明，这里构造内容
    msg['Subject'] = sub
    msg['From'] = _format_addr('来自火星的小朋友<%s>'%mail_user)   #这里定义的发送人的在邮件显示的名字
    msg['To'] = to_list
    try:
        server = smtplib.SMTP_SSL(mail_host)
        server.connect(mail_host, port=465)
        # server.starttls()
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except:
        return False
    
    
#*************定义MYSQL数据库读取函数*************#
def Read_database (user_name,password,address,port,database_name,sql):
    conn = pymysql.connect(host = address,user = user_name,passwd = password,\
                           db = database_name , port = int(port) ,charset = "utf8mb4")
    try:
        df = pd.read_sql (sql,con = conn)
    except:
        print ('\n Reading Error  \n')    
    finally:
        conn.close()
    print ('\n Completion of data reading \n')    
    return (df) 


def _goodmonring1():
#内容爬取
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
    setword = list[0].get("word")
    setimage = list[0].get("image")
    setdata =list[0].get("date")
    return setimage


def _goodmonring2():
#内容爬取
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
    setword = list[0].get("word")
    setimage = list[0].get("image")
    setdata =list[0].get("date")
    return setdata
    
    

#*************定义天气信息爬取函数*************#
def _weather(url,word,setimage,setdata,vedio_str):
    
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
    final = final_list[1]
    riqi=final[0]
    tianqi =final[1]
    temtop =final[2]
    temtod =final[3]
    message =  """
    <!DOCTYPE HTML>
    <html>
    <head>
    <meta charset="utf-8"/>
    <title>段落缩进</title>
    <style>
        .p1{text-indent: 40px;}
        .p2{text-indent: 3em;}
    </style>
    <script type="text/javascript">
        var audioTag = document.createElement('audio');
        if (!(!!(audioTag.canPlayType) && ("no" != audioTag.canPlayType("audio/mpeg")) && ("" != audioTag.canPlayType("audio/mpeg")))) {
            AudioPlayer.embed("audioplayer_1", {soundFile: "your.mp3", transparentpagebg: "yes"});
            $( '#audioplayer').hide();
     }
        else 
        {
            $( '#audioplayer' ).audioPlayer();
        }
    </script>
    </head>
    <body>
        <p><img src="%s"></p>
        <p>%s</p>
        <p> </p>
        <p style="text-align:left">欢迎收听今天夜读！</p>
        <p id="audioplayer_1"></p>
        <audio id="audioplayer" preload="auto" controls style="width:380px" >
        <source src="%s" type="audio/mp3">
        </audio>
        <p style="text-align:left">明日天气：%s</p>
        <p style="text-align:left">最高温度：%s ℃</p>
        <p style="text-align:left">最低温度：%s ℃</p>
        <p style="text-align:right">晚安！   </p>
        <p style="text-align:right">%s</p>
        </body>
    </html>
    """%(setimage,word,vedio_str,final[1],final[2],final[3],setdata)
    return message 

#*************定义文字处理+调用seng_email发送函数*************#
def text_send(people_df,weather_df,words_df):
    now_time = datetime.datetime.now()
    str=datetime.datetime.now().strftime('%Y-%m-%d')
    vedio_str="http://qfile.k6366.com.cn/"+str+".mp3"
    words=words_df.values
    db=people_df.values
    db2=weather_df.values
    sui=random.randint(0,2639)
    list=[]
    list1=[]
    for a in words[sui][0]:
        list.append(a)
    #print(list)
    for a in range(len(list)):
        if (list[a]=='b') or (list[a]=='f'):
            break
        else:
            list1.append(list[a])
    word=''.join(list1)
    for a in db:
        to_addrs=a[2]
        city=a[1]
        #print (to_addrs)
        url=None
        for b in db2:
            if b[0]==city:
                url=b[1]
                print(url)
                break
        if url != None:
            neirong=_weather(url,word,_goodmonring1(),_goodmonring2(),vedio_str)
            send_mail(to_addrs,"晚安鸭!",neirong)
            print (to_addrs+" success")
            time.sleep(10)
        else:
            print (to_addrs+" err")
    
#*************定义一个定时的job函数*************#    
def main():   
    people_df = Read_database (user_name,password,address,port,'users',''' SELECT * from test; ''' )
    weather_df = Read_database (user_name,password,address,port,'weather',''' SELECT * from weather; ''')
    words_df = Read_database (user_name,password,address,port,'words',''' SELECT * from word; ''')
    text_send(people_df,weather_df,words_df)

#schedule.every(5).minutes.do(main)       #部署每10分钟执行一次job()函数的任务
#schedule.every().day.at("23:00").do(main) #部署在每天的10:30执行job()函数的任务
#while True:
#    schedule.run_pending()
#    time.sleep(1)    


if __name__ == "__main__":
    main()

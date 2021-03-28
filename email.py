#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import requests
import string
import json
import pandas as pd
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText


#*************定义邮件全局字段*************#

mail_host="smtp.qq.com"           #设置代理服务器，QQ邮箱，网易邮箱等
mail_user="2440229611@qq.com"     #用户名
mail_pass=""      #邮件口令


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
    
    

#*************定义html构建函数*************#
def get_html(cityname):
    url = 'https://service-4ua9qtvz-1258693536.sh.apigw.tencentcs.com/release/api'
    #url = 'https://service-4ua9qtvz-1258693536.sh.apigw.tencentcs.com/release/api2'
    #url = 'http://lean-api.wxiou.cn/api'
    #url = 'http://lean-api.wxiou.cn/api2'
    datas ={
        'cityname':cityname
    }
    response = requests.get(url=url,data=datas)
    datas = json.loads(response.text)
    print(datas)

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
    """%(datas['image'],datas['word'],datas['voice'],datas['weather'][1],datas['weather'][2],datas['weather'][3],datas['date'])
    return message 

#*************定义文字处理+调用seng_email发送函数*************#
def mail_send():
    
    cityname = "nanjing"
    to_addrs = "2xxxxxx@qq.com"
    
    html = get_html(cityname)
    if send_mail(to_addrs,"晚安鸭!",html) = True:
        print (to_addrs+" success")
    else:
        print("error")

        
if __name__ == "__main__":
    mail_send()

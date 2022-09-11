# -*- coding:utf-8 -*-
import json
import smtplib
import requests
import string
import json
from bmob import *
import bmob
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText


#*************定义邮件全局字段*************#

mail_host="smtp.qq.com"           #设置代理服务器，QQ邮箱，网易邮箱等
mail_user="xxxxx@qq.com"     #用户名
mail_pass="xxxxxxxxxxx"      #邮件口令


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
    except Exception as e:
        print("报错信息如下：")
        print(e)
        return False
    
    

#*************定义html构建函数*************#
def get_html():
    #url = 'https://service-4ua9qtvz-1258693536.sh.apigw.tencentcs.com/release/api'
    url = 'http://lean-api.wxiou.cn/api'
    #url = 'https://e.ioer.cc/api'
    datas ={
        'key':'防止接口乱用'
    }
    response = requests.post(url=url,data=datas)
    datas = json.loads(response.text)
    # print(datas)
    for data in datas['data']:
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
        """%(data[1],data[2],data[4],data[6],data[7],data[8],data[3])
        
        try:
            to_addrs = data[0]

            view = send_mail(to_addrs,"晚安鸭!",message)

            if view == False:
                view2 = send_mail(to_addrs,"晚安鸭!",message)
                if view2 == False:
                    send_mail(to_addrs,"晚安鸭!",message)

        except Exception as e:
            print(e)

    return 0

#*************发送函数*************#
def handler (event, context):
    get_html()

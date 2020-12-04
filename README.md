# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Python
def text_push(data):
    """消息推送.
    完成消息队列中定时任务的消息推送.
    Date:
        2020-12-04
    Author:
        NJUPT-B18150118 YWX
    Args:
        data: 需要推送的Json格式消息.
    Returns:
        None.
    Raises:
        IOError: None.
    """ 
    # 获取推送信息
    text = data['title']
    time_year = time.localtime().tm_year
    time_month = data['time'][5]+data['time'][6]
    time_day = data['time'][8]+data['time'][9]
    time_hour = data['time'][11]+data['time'][12]
    time_min =data['time'][14]+data['time'][15]
    
    # 构造消息格式
    qq_text="     【今日提醒任务】     \n"+"🕙:    "+str(time_year)+"-"+str(time_month)+"-"+str(time_day)+" "+str(time_hour)+":"+str(time_min)+":00"+"\n"+"🍄:    "+text+"\n"
    wechat_text="     【🕙:    "+str(time_year)+"-"+str(time_month)+"-"+str(time_day)+" "+str(time_hour)+":"+str(time_min)+":00】"+"\n\n"+"     【🍄:    "+text+"】     \n"
    
    # 消息推送
    if len(data['sendId']) == 55:
        """微信公众号消息推送"""
        sckey = data['sendId']
        title = "【今日任务提醒】"
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+title+'&desp=' + wechat_text)
    else:
        spkey = data['sendId']
        """QQ号消息推送""" 
        cpurl = 'https://push.xuthus.cc/send/'+spkey    #发送方式，我用的send
        requests.post(cpurl,qq_text.encode('utf-8'))         #把天气数据转换成UTF-8格式，不然要报错。 
```

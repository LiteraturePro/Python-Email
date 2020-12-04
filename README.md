# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Python
def Data_dispose():
    """ 获取本地时间（云函数系统时间与实际时间相差8个小时）与数据库中时间字段进行比对，符合条件则推送，不符合条件则跳过.
    Date:
        2020-12-04
    Author:
        NJUPT-B18150118 YWX
    Args:
        None.
    Returns:
        返回message.
    Raises:
        IOError: None.
    """
    # 调用查询函数得到数据
    datas = GetData()
    
    message = "你好"
    
     # 处理Severless中系统时间比实际时间少8个小时
    if time.localtime().tm_hour <= 16:
        time_hour = time.localtime().tm_hour+8
    elif time.localtime().tm_hour == 17:
        time_hour = 1
    elif time.localtime().tm_hour == 18:
        time_hour = 2
    elif time.localtime().tm_hour == 19:
        time_hour = 3
    elif time.localtime().tm_hour == 20:
        time_hour = 4
    elif time.localtime().tm_hour == 21:
        time_hour = 5
    elif time.localtime().tm_hour == 22:
        time_hour = 6
    elif time.localtime().tm_hour == 23:
        time_hour = 7
    elif time.localtime().tm_hour == 24:
        time_hour = 8
    else :
        print("假的吧，还有这事?")
        
    # 格式化时间戳为本地的时间
    time_year = time.localtime().tm_year
    time_month = time.localtime().tm_mon
    time_day = time.localtime().tm_mday
    time_min = time.localtime().tm_min
    
    
    # 循环检查列表消息
    for data in datas:
        data_year = data['time'][0]+data['time'][1]+data['time'][2]+data['time'][3]
        data_month = data['time'][5]+data['time'][6]
        data_day = data['time'][8]+data['time'][9]
        data_time = data['time'][11]+data['time'][12]
        data_min =data['time'][14]+data['time'][15]
        
        # 时间差处理
        time_diff = int(data_min)-time_min
        
        if int(data_year) == time_year and int(data_month) == time_month and int(data_day) == time_day and int(data_time) == time_hour and (time_diff > 0) and (time_diff <= 1):
            
            # 调用推送
            text_push(data)
            
            # 更新数据
            Updata("InfomationReq",data['objectId'])
            
            message = data['objectId']+"推送成功"
        else:
            message = "时间没到"
        
    return message
```

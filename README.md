# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Python
def GetData():
    """ 查询并返回所有符合条件的数据.
    Date:
        2020-12-04
    Author:
        NJUPT-B18150118 YWX
    Args:
        None.
    Returns:
        datas['results']: 返回按条件查询的的数据信息的results字段.
    Raises:
        IOError: None.
    """
    datas = bmobs.find( # 查找数据库
            "InfomationReq", #表名
        where=BmobQuerier().addWhereEqualTo("did", "未推送")
        ).jsonData
    return datas['results']
```

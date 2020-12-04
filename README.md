# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Python
def Updata(table,objectId):
    """ 以objectId为唯一标识更新一条数据
    Date:
        2020-12-04
    Author:
        NJUPT-B18150118 YWX
    Args:
        table: 文档型数据库中的数据表.
        objectId: 数据库中一条消息的唯一身份ID.
    Returns:
        返回bmobs.update的状态值.
    Raises:
        IOError: None.
    """
    return bmobs.update(
            table, # 表名
            objectId,
                {
                    'did': '已推送'
                }
        ).jsonData # 输出json格式的内容
```

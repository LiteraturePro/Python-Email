# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java

/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   Person
 * @Package  com.njupt.wtime.bean
 * @Description:  定义Person类继承自BmobObject类
 * @author:  杨文旋
 * @date:   2020.12.02
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */
public class Person extends BmobObject {
    private String name;     //姓名
    private String password;  //密码

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
```

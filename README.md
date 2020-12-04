# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java

/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   RegisterUser
 * @Package  com.njupt.wtime.bean
 * @Description:  定义RegisterUser类继承自BmobObject类，用户注册类
 * @author:  杨文旋
 * @date:   2020.12.02
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */
public class RegisterUser extends BmobObject {
    private String registerName;      //注册用户名
    private String registerPassword;  //注册密码

    public String getRegisterName() {
        return registerName;
    }

    public void setRegisterName(String registerName) {
        this.registerName = registerName;
    }

    public String getRegisterPassword() {
        return registerPassword;
    }

    public void setRegisterPassword(String registerPassword) {
        this.registerPassword = registerPassword;
    }
}

```

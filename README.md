# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   InfomationReq
 * @Package  com.njupt.wtime.bean
 * @Description:  定义InfomationReq类继承自BmobObject类，推送信息的类
 * @author:  杨文旋
 * @date:   2020.12.02
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */

public class InfomationReq extends BmobObject{

    private String title;    //推送内容
    private String sendId;   //推送识别码
    private String time;     //推送时间
    private String did;      //推送标记

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getsendId() {
        return sendId;
    }

    public void setsendId(String sendId) {
        this.sendId = sendId;
    }

    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public String getDid() {
        return did;
    }

    public void setDid(String did) {
        this.did = did;
    }
}
```

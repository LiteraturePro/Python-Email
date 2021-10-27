# Python-Email
## Python版邮件推送，后端API已经构建完成，邮件中所涉及的数据，均由API提供，音频、图片等数据版权归原作者所有。

## 客户端

使用本仓库的email.py代码调用后端服务发信即可。

## 服务器端

服务器端提供了音频，图片，文件。天气等数据服务，通过调用API即可获取，后端代码暂不开源。后端部署在Leancloud云引擎上，由于不是很稳定，又同时部署在腾讯云函数上，提供的两个API接口均可调用。下面是后端服务，点击链接即可查看相关页面和接口说明。

The webapi is deployed Leancloud here - http://lean-api.wxiou.cn/

The webapi is deployed Tencent Serverless here -
![](https://pcdn.wxiou.cn/20210407201747.png)
![](https://pcdn.wxiou.cn/20210328182145.png)


## 使用

首先，拿到你的邮件口令（不会就百度），填入Python脚本的相应处，同时修改`mail_user`为你的发信方，`to_addrs`修改为你的收信方。`cityname`修改为你的收信方所在的城市的拼音字段，运行就行了。


## 效果
<img src="https://pcdn.wxiou.cn/20210328183834.jpg" alt="图片替换文本" width="180" height="360" align="bottom" /><img src="https://pcdn.wxiou.cn/20210328183850.jpg" alt="图片替换文本" width="180" height="360" align="bottom" />


## 后期

暂时先这样吧，可以多用户的，你自己改一下就好了。太懒了现在。

# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
package com.njupt.wtime;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import com.njupt.wtime.bean.RegisterUser;
import java.util.List;
import cn.bmob.v3.BmobQuery;
import cn.bmob.v3.BmobUser;
import cn.bmob.v3.exception.BmobException;
import cn.bmob.v3.listener.FindListener;
import cn.bmob.v3.listener.SaveListener;

/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   RegisterActivity
 * @Package  com.njupt.wtime
 * @Description:  定义RegisterActivity类继承自Activity类
 * @author:  杨文旋
 * @date:   2020.12.03
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */

public class RegisterActivity extends Activity implements View.OnClickListener {


    private EditText accountRegisterName;
    private EditText accountRegisterPassword;
    private Button registerBtn;
    private TextView registerBackBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        /**加载xml文件*/
        setContentView(R.layout.register_account);

        initView();
        initData();
        initListener();
    }


    /*** 定义初始化函数
     * @author NJUPT-B18150118
     * @version 1.0
     * @use  进行一些初始化的定义，把他们都放在一个initView里面，然后直接调用这个函数就可以完成初始化了
     */
    private void initView() {
        accountRegisterName = (EditText) findViewById(R.id.i8_accountRegister_name);
        accountRegisterPassword = (EditText) findViewById(R.id.i8_accountRegister_password);
        registerBtn = (Button) findViewById(R.id.i8_accountRegistern_toRegister);
        registerBackBtn = (TextView) findViewById(R.id.register_back_btn);
    }

    private void initData() {}

    /*** 定义监听函数
     * @author NJUPT-B18150118
     * @version 1.0
     * @use  进行页面监听，等待用户操作
     */
    private void initListener() {

        registerBtn.setOnClickListener(this);
        registerBackBtn.setOnClickListener(this);
    }

    @Override
    /**  监听按钮动态
     * @author NJUPT-B18150118
     * @version 1.0
     */
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.i8_accountRegistern_toRegister:
                /**点击登录，调用注册函数*/
                bmobRegisterAccount();
                break;
            case R.id.register_back_btn:
                /**点击返回登录页面*/
                Intent intent = new Intent(RegisterActivity.this, LoginActivity.class);
                startActivity(intent);
            default:
                break;
        }
    }

    /**  bmob注册账号
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void bmobRegisterAccount() {
        final String registerName = accountRegisterName.getText().toString().trim();
        final String registerPassword = accountRegisterPassword.getText().toString().trim();

        if (TextUtils.isEmpty(registerName) || TextUtils.isEmpty(registerPassword)) {
            showToast("注册账号或密码为空");
            return;
        }


        /**BmobUser类为Bmob后端云提供类*/
        BmobUser bmobUser = new BmobUser();
        bmobUser.setUsername(registerName);
        bmobUser.setPassword(registerPassword);
        bmobUser.signUp(new SaveListener<BmobUser>() {
            @Override
            public void done(BmobUser bmobUser, BmobException e) {
                if (e == null) {
                    showToast("恭喜，注册账号成功");
                    finish();
                } else {
                    showToast("register fail:" + e.getMessage());
                }
            }
        });
    }

    /**
     * 账号注册
     */
    private void registerAccount() {
        final String registerName = accountRegisterName.getText().toString().trim();
        final String registerPassword = accountRegisterPassword.getText().toString().trim();

        if (TextUtils.isEmpty(registerName) || TextUtils.isEmpty(registerPassword)) {
            showToast("注册账号或密码为空");
            return;
        }

        /**已存在账号的查询*/
        BmobQuery<RegisterUser> registerUserBmobQuery = new BmobQuery<>();
        registerUserBmobQuery.order("-createdAt");
        registerUserBmobQuery.findObjects(new FindListener<RegisterUser>() {
            @Override
            public void done(List<RegisterUser> lists, BmobException e) {
                for (RegisterUser list : lists) {
                    if (registerName.equals(list.getRegisterName())) {
                        showToast("账号已被注册，请重新输入");
                    } else {
                        registerAccount(registerName, registerPassword);
                    }
                }
            }
        });
    }


    /**
     * 注册账号，将用户账号密码添加进数据库
     * @author NJUPT-B18150118
     * @param registerName     注册名
     * @param registerPassword 密码
     */
    private void registerAccount(String registerName, String registerPassword) {
        RegisterUser registerUser = new RegisterUser();
        registerUser.setRegisterName(registerName);
        registerUser.setRegisterPassword(registerPassword);
        registerUser.save(new SaveListener<String>() {
            @Override
            public void done(String s, BmobException e) {
                if (e == null) {
                    showToast("恭喜，注册账号成功");
                    finish();
                } else {
                    showToast("注册账号失败");
                }
            }
        });
    }

    /**
     * @author NJUPT-B18150118
     * @version 1.0
     * @param msg 打印信息
     */
    private void showToast(String msg) {
        Toast.makeText(this, msg, Toast.LENGTH_SHORT).show();
    }
}

```

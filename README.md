# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   LoginActivity
 * @Package  com.njupt.wtime
 * @Description:  定义LoginActivity类继承自Activity类
 * @author:  杨文旋
 * @date:   2020.12.03
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */

public class LoginActivity extends Activity implements View.OnClickListener {
    private EditText accountLoginName;
    private EditText accountLoginPassword;
    private Button loginBtn;
    private TextView registerAccountBtn;
    private ProgressBar progressBar;
    private LinearLayout llLogin;



    @Override
    /*** 创建登录页面
     * @author NJUPT-B18150118
     * @version 1.0
     */
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        /**加载xml文件*/
        setContentView(R.layout.login_accountlogin);
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
        accountLoginName = (EditText) findViewById(R.id.i8_accountLogin_name);
        accountLoginPassword = (EditText) findViewById(R.id.i8_accountLogin_password);
        loginBtn = (Button) findViewById(R.id.i8_accountLogin_toLogin);
        registerAccountBtn = (TextView) findViewById(R.id.register_account_btn);
        progressBar = (ProgressBar) findViewById(R.id.pb);
        llLogin = (LinearLayout) findViewById(R.id.ll_login);
    }

    private void initData() {}

    /*** 显示进度条
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void showProgressBar() {
        progressBar.setVisibility(View.VISIBLE);
        llLogin.setVisibility(View.GONE);
    }


    /*** 隐藏进度条
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void hiddenProgressBar() {
        progressBar.setVisibility(View.GONE);
        llLogin.setVisibility(View.VISIBLE);
    }

    /*** 定义监听函数
     * @author NJUPT-B18150118
     * @version 1.0
     * @use  进行页面监听，等待用户操作
     */
    private void initListener() {
        loginBtn.setOnClickListener(this);
        registerAccountBtn.setOnClickListener(this);
    }

    @Override
    /**  监听按钮动态
     * @author NJUPT-B18150118
     * @version 1.0
     */
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.i8_accountLogin_toLogin:
                /**点击登录，调用登录函数*/
                bmobUserAccountLogin();
                break;
            case R.id.register_account_btn:
                /**点击注册，跳转到注册界面*/
                Intent intent = new Intent(LoginActivity.this, RegisterActivity.class);
                startActivity(intent);
                break;
            default:
                break;
        }
    }

    private void bmobUserAccountLogin() {

        final String accountName = accountLoginName.getText().toString().trim();
        final String accountPassword = accountLoginPassword.getText().toString().trim();

        if (TextUtils.isEmpty(accountName)) {
            showToast("账号不能为空");
            return;
        }

        if (TextUtils.isEmpty(accountPassword)) {
            showToast("密码不能为空");
            return;
        }

        /**显示进度条*/
        showProgressBar();
        /**登录过程*/
        new Handler().postDelayed(new Runnable() {
            @Override
            public void run() {

                /**BmobUser类为Bmob后端云提供类*/
                BmobUser bmobUser = new BmobUser();
                bmobUser.setUsername(accountName);
                bmobUser.setPassword(accountPassword);

                bmobUser.login(new SaveListener<BmobUser>() {
                    @Override
                    public void done(BmobUser bmobUser, BmobException e) {
                        if (e == null) {
                            /**登录成功后进入主界面*/
                            Intent intent = new Intent(LoginActivity.this, WtimeActivity.class);
                            startActivity(intent);
                            finish();
                        } else {
                            showToast(""+e.getMessage());
                            /**隐藏进度条*/
                            hiddenProgressBar();
                        }
                    }
                });
            }
        }, 3000);
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

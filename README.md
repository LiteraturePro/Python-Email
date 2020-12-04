# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   ShowInfoActivity
 * @Package  com.njupt.wtime
 * @Description:  定义ShowInfoActivity类继承自Activity类
 * @author:  杨文旋
 * @date:   2020.12.03
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */


public class ShowInfoActivity extends Activity  {
    private ImageView back;
    private ImageView add;
    private EditText title;
    private EditText sendid;
    private EditText time;
    private InfomationReq infomationReq;
    private WebView OBDmwebView;
    private Button thankBtn;
    @SuppressLint("JavascriptInterface")


    @Override
    /*** 创建页面
     * @author NJUPT-B18150118
     * @version 1.0
     */
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_show_info);
        initView();
        initData();
        sendid.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {}
        });
        ImageView thank_png = new ImageView(ShowInfoActivity.this);
        thank_png.setImageResource(R.drawable.wechatpay);
        final PopupWindow popupWindow = new PopupWindow(thank_png,500,500);
        popupWindow.setOutsideTouchable(true);
        //监听关注按钮
        thankBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                popupWindow.showAsDropDown(thankBtn);
            }
        });
        //加载留言插件
        OBDmwebView = this.findViewById(R.id.obd_webview);
        OBDmwebView.getSettings().setJavaScriptEnabled(true);   //启用Javascript
        OBDmwebView.loadUrl("file:///android_asset/index.html");  //加载文件的路径以及文件名
        OBDmwebView.addJavascriptInterface(this,"web");

    }

    /*** 初始化数据
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initData() {
        infomationReq = (InfomationReq) getIntent().getSerializableExtra("showData");
        if (infomationReq != null) {
            title.setText(infomationReq.getTitle());
            sendid.setText(infomationReq.getsendId());
            time.setText(infomationReq.getTime());
        }
    }

    /*** 注册组件
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initView() {
        back = (ImageView) findViewById(R.id.iv_back_show);
        add = (ImageView) findViewById(R.id.iv_add_show);
        title = (EditText) findViewById(R.id.et_title_show);
        sendid = (EditText) findViewById(R.id.et_phone_num_show);
        time = (EditText) findViewById(R.id.et_desc_show);
        title.setFocusable(false);//设置为不可编辑
        time.setFocusable(false);//设置为不可编辑
        sendid.setFocusable(false);//设置为不可编辑
        thankBtn = (Button) findViewById(R.id.thank);
    }
}
```

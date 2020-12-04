# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   AddInformationActivity
 * @Package  com.njupt.wtime
 * @Description:  定义AddInformationActivity类继承自Activity类
 * @author:  杨文旋
 * @date:   2020.12.03
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */

public class AddInformationActivity extends Activity implements View.OnClickListener {

    private ImageView back;
    private ImageView add;
    private EditText title;
    private EditText SEND_ID;
    private Button time;
    private InfomationReq infomationReq;
    private boolean isChangeInfos;
    private TimePickerView pvTime;
    private String displayedText;

    @Override
    /*** 创建页面
     * @author NJUPT-B18150118
     * @version 1.0
     */
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.add_infos_activity);

        initView();
        initData();
        initTimePicker();
        //注册时间选择器
        Button btn_Time = (Button) findViewById(R.id.btn_Time);
        btn_Time.setOnClickListener(this);
        initListener();
    }

    /*** 注册组件
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initView() {
        back = (ImageView) findViewById(R.id.iv_back);
        add = (ImageView) findViewById(R.id.iv_add);
        title = (EditText) findViewById(R.id.et_title);
        SEND_ID = (EditText) findViewById(R.id.et_id_num);
        time =(Button) findViewById(R.id.btn_Time);
    }

    /*** 初始数据
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initData() {
        infomationReq = (InfomationReq) getIntent().getSerializableExtra("editData");
        if (infomationReq != null) {
            isChangeInfos = true;//设置是否是信息更新操作
            title.setText(infomationReq.getTitle());
            SEND_ID.setText(infomationReq.getsendId());
        }
    }

    private void initListener() {
        back.setOnClickListener(this);
        add.setOnClickListener(this);
    }

    @Override
    /*** 监听按钮
     * @author NJUPT-B18150118
     * @version 1.0
     */
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.iv_back:
                finish();
                break;
            case R.id.iv_add:
                addData();
                break;
            case R.id.btn_Time:
                pvTime.show(v);//弹出时间选择器，传递参数过去，回调的时候则可以绑定此view
                break;
            default:
                break;
        }
    }
    /*** 添加信息
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void addData() {
        String titleName = title.getText().toString().trim();
        String Num = SEND_ID.getText().toString().trim();

        if (TextUtils.isEmpty(titleName)) {
            showToast("内容不能为空");
            return;
        }

        if (TextUtils.isEmpty(Num)) {
            showToast("推送ID不能为空");
            return;
        }
        //判断是发表新的信息还是更改信息，然后调用相应的函数
        if (isChangeInfos) {
            updataInfo(titleName, Num, displayedText,"未推送");
        } else {
            publishLostInfo(titleName, Num, displayedText,"未推送");
        }
    }
    /** 数据更新
     * @author NJUPT-B18150118
     * @version 1.0
     * @param titleName 推送内容
     * @param num     推送ID
     * @param time 推送时间
     * @param did  推送标记
     */
    private void updataInfo(String titleName, String num, String time,String did) {
        InfomationReq InfomationReq = new InfomationReq();
        InfomationReq.setTitle(titleName);
        InfomationReq.setsendId(num);
        InfomationReq.setTime(time);
        InfomationReq.setDid(did);
        InfomationReq.update(infomationReq.getObjectId(), new UpdateListener() {
            @Override
            public void done(BmobException e) {
                if (e == null) {
                    showToast("更新信息成功");
                    //更新数据后提示主界面进行数据刷新
                    Intent intent = new Intent();
                    setResult(RESULT_OK, intent);
                    finish();
                }
            }
        });
    }

    /** 数据添加
     * @author NJUPT-B18150118
     * @version 1.0
     * @param titleName 推送内容
     * @param num     推送ID
     * @param time 推送时间
     * @param did  推送标记
     */
    private void publishLostInfo(String titleName, String num, String time,String did) {
        InfomationReq InfomationReq = new InfomationReq();
        InfomationReq.setTitle(titleName);
        InfomationReq.setsendId(num);
        InfomationReq.setTime(time);
        InfomationReq.setDid(did);
        InfomationReq.save(new SaveListener<String>() {
            @Override
            public void done(String s, BmobException e) {
                if (e == null) {
                    showToast("事件设置成功");
                    //成功后提示主界面刷新数据
                    Intent intent = new Intent();
                    setResult(RESULT_OK, intent);
                    //成功后将页面销毁
                    finish();
                } else {
                    showToast("事件设置失败");
                }
            }
        });
    }
    /** 时间五级联动选择器
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initTimePicker() {//Dialog 模式下，在底部弹出
        pvTime = new TimePickerBuilder(this, new OnTimeSelectListener() {
            @Override
            public void onTimeSelect(Date date, View v) {
                Toast myToast = Toast.makeText(AddInformationActivity.this, getTime(date), Toast.LENGTH_SHORT);
                myToast.show();
                displayedText = ((TextView)((LinearLayout)myToast.getView()).getChildAt(0)).getText().toString();
                Log.i("pvTime", "onTimeSelect");

            }
        })
                .setTimeSelectChangeListener(new OnTimeSelectChangeListener() {
                    @Override
                    public void onTimeSelectChanged(Date date) {
                        Log.i("pvTime", "onTimeSelectChanged");
                    }
                })
                .setType(new boolean[]{true, true, true, true, true, true})
                .isDialog(true) //默认设置false ，内部实现将DecorView 作为它的父控件。
                .addOnCancelClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Log.i("pvTime", "onCancelClickListener");
                    }
                })
                .setItemVisibleCount(5) //若设置偶数，实际值会加1（比如设置6，则最大可见条目为7）
                .setLineSpacingMultiplier(2.0f)
                .isAlphaGradient(true)
                .build();

        Dialog mDialog = pvTime.getDialog();
        if (mDialog != null) {

            FrameLayout.LayoutParams params = new FrameLayout.LayoutParams(
                    ViewGroup.LayoutParams.MATCH_PARENT,
                    ViewGroup.LayoutParams.WRAP_CONTENT,
                    Gravity.BOTTOM);

            params.leftMargin = 0;
            params.rightMargin = 0;
            pvTime.getDialogContainerLayout().setLayoutParams(params);

            Window dialogWindow = mDialog.getWindow();
            if (dialogWindow != null) {
                dialogWindow.setWindowAnimations(R.style.picker_view_slide_anim);//修改动画样式
                dialogWindow.setGravity(Gravity.BOTTOM);//改成Bottom,底部显示
                dialogWindow.setDimAmount(0.3f);
            }
        }
    }
    /** 时间选择器的时间类型自定义函数
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private String getTime(Date date) {//可根据需要自行截取数据显示
        Log.d("getTime()", "choice date millis: " + date.getTime());
        SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        return format.format(date);
    }

    /**
     * @param msg 打印信息
     */
    private void showToast(String msg) {
        Toast.makeText(this, msg, Toast.LENGTH_SHORT).show();
    }
}
```

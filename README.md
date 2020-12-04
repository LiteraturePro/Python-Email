# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
/**
 * All rights Reserved, Designed By NJUPT-B18150118
 * @Title:   WtimeActivity
 * @Package  com.njupt.wtime
 * @Description:  定义WtimeActivity类继承自Activity类
 * @author:  杨文旋
 * @date:   2020.12.03
 * @version  V1.0
 * @Copyright:  2020-2022 @njupt.edu.cn Inc. All rights reserved.
 */

public class WtimeActivity extends Activity implements View.OnClickListener, WtimeAdapter.ItemClickListener {

    private RecyclerView recyclerView;
    private ImageView addBtn;
    private WtimeAdapter WtimeAdapter;
    private long exitTime = 0;
    private final static int REQUEST_CODE = 999;
    private List<InfomationReq> InfomationReqList;
    //加功能
    private TextView info_title;

    @Override
    /** 创建页面
     * @author NJUPT-B18150118
     * @version 1.0
     */
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.wtime_main_activity);
        /**注册腾讯云推送插件*/
        /**该推送形式还没实现*/
        XGPushConfig.enableDebug(this,false);
        XGPushManager.registerPush(this, new XGIOperateCallback() {
            @Override
            public void onSuccess(Object data, int flag) {
                //token在设备卸载重装的时候有可能会变
                Log.d("TPush", "注册成功，设备token为：" + data);
            }

            @Override
            public void onFail(Object data, int errCode, String msg) {
                Log.d("TPush", "注册失败，错误码：" + errCode + ",错误信息：" + msg);
            }
        });
        initView();
        initData();
        initListener();
        //点击显示详情
        info_title = (TextView) LayoutInflater.from(WtimeActivity.this).inflate(R.layout.time_item, null).findViewById(R.id.tv_title);
        info_title.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent_show = new Intent(WtimeActivity.this, ShowInfoActivity.class);
               startActivity(intent_show);
            }
        }
        );
    }
    /** 注册WtimeAdapter适配器
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initView() {
        recyclerView = (RecyclerView) findViewById(R.id.rl_recyclerview);
        addBtn = (ImageView) findViewById(R.id.iv_add);
        recyclerView.setLayoutManager(new LinearLayoutManager(this, LinearLayoutManager.VERTICAL, false));
        WtimeAdapter = new WtimeAdapter(WtimeActivity.this);
        WtimeAdapter.setLongClickListener(this);

    }
    /** 初始化数据信息
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void initData() {
        BmobQuery<InfomationReq> InfomationReqBmobQuery = new BmobQuery<>();
        InfomationReqBmobQuery.order("-updatedAt");//排序
        InfomationReqBmobQuery.findObjects(new FindListener<InfomationReq>() {
            @Override
            public void done(List<InfomationReq> list, BmobException e) {
                if (e == null) {
                    InfomationReqList = list;
                    WtimeAdapter.setData(list);
                    recyclerView.setAdapter(WtimeAdapter);
                } else {
                    showToast("查询数据失败");
                }
            }
        });
    }

    private void initListener() {
        addBtn.setOnClickListener(this);
    }

    /**
     * @param msg 打印信息
     */
    private void showToast(String msg) {
        Toast.makeText(this, msg, Toast.LENGTH_SHORT).show();
    }

    @Override
    /** 监听按钮
     * @author NJUPT-B18150118
     * @version 1.0
     */
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.iv_add:
                Intent intent = new Intent(WtimeActivity.this, AddInformationActivity.class);
                startActivityForResult(intent, REQUEST_CODE);
                break;
            case R.id.tv_title:
                Intent intent_show = new Intent(WtimeActivity.this, ShowInfoActivity.class);
                startActivity(intent_show);
                break;
            default:
                break;
        }
    }

    @Override
    /** 数据刷新
     * @author NJUPT-B18150118
     * @version 1.0
     */
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        switch (requestCode) {
            case REQUEST_CODE:
                if (resultCode == RESULT_OK) {
                    refreshData();//数据刷新
                }
                break;
            default:
                break;
        }
    }

    /** 查询最新的数据
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void refreshData() {
        BmobQuery<InfomationReq> InfomationReqBmobQuery = new BmobQuery<>();
        InfomationReqBmobQuery.order("-updatedAt");//按更新时间排序
        InfomationReqBmobQuery.findObjects(new FindListener<InfomationReq>() {
            @Override
            public void done(List<InfomationReq> list, BmobException e) {
                if (e == null) {
                    InfomationReqList = list;
                    WtimeAdapter.setData(list);
                    WtimeAdapter.notifyDataSetChanged();
                }
            }
        });
    }

    @Override
    /** 返回按钮退出
     * @author NJUPT-B18150118
     * @version 1.0
     */
    public boolean onKeyDown(int keyCode, KeyEvent event) {

        if (keyCode == KeyEvent.KEYCODE_BACK) {
            if (System.currentTimeMillis() - exitTime > 2000) {
                showToast("再按一次退出程序");
                exitTime = System.currentTimeMillis();
            } else {
                android.os.Process.killProcess(android.os.Process.myPid());
            }
        }
        return false;
    }

    @Override
    /** 三段按钮逻辑函数
     * @author NJUPT-B18150118
     * @version 1.0
     */
    public void onEditOrDeleteClick(int position, int code) {

        if (code == WtimeAdapter.EDIT_CODE) {
            Intent intent = new Intent(WtimeActivity.this, AddInformationActivity.class);
            Bundle bundle = new Bundle();
            bundle.putSerializable("editData", InfomationReqList.get(position));
            intent.putExtras(bundle);
            startActivityForResult(intent, REQUEST_CODE);
        } else if (code == WtimeAdapter.DELETE_CODE) {
            deleteItemData(position);
        }else if (code == WtimeAdapter.OPEN_CODE){
            Toast.makeText(WtimeActivity.this,"\\0^◇^0/",Toast.LENGTH_LONG).show();
//            Intent intent_show = new Intent(LostAndFoundActivity.this, ShowInfoActivity.class);
//            startActivity(intent_show);
            Intent intent = new Intent(WtimeActivity.this, ShowInfoActivity.class);
            Bundle bundle = new Bundle();
            bundle.putSerializable("showData", InfomationReqList.get(position));
            intent.putExtras(bundle);
            startActivityForResult(intent, REQUEST_CODE);
        }
    }
    /** 数据删除函数
     * @author NJUPT-B18150118
     * @version 1.0
     */
    private void deleteItemData(final int position) {
        if (InfomationReqList.size() != 0) {
            InfomationReq InfomationReq = new InfomationReq();
            InfomationReq.setObjectId(InfomationReqList.get(position).getObjectId());
            InfomationReq.delete(new UpdateListener() {
                @Override
                public void done(BmobException e) {
                    if (e == null) {
                        InfomationReqList.remove(position);
                        WtimeAdapter.setData(InfomationReqList);
                        WtimeAdapter.notifyDataSetChanged();
                    } else {
                        showToast("删除数据失败");
                    }
                }
            });
        }
    }
}
```

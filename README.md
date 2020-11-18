# Python-Email
Python版邮件推送，涉及Mysql , 云函数。

```Java
package cn.edu.njupt;

public class Add {
	public int add(int para1, int para2) {
        return para1 + para2;
	}

}

```

```Java
package cn.edu.njupt;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

import java.util.Arrays;
import java.util.Collection;
import static org.junit.Assert.assertEquals;


@RunWith(Parameterized.class)  //利用我们指定的运行器运行测试

public class AddTest {

	private int para1;
    private int para2;  
    private int expected;  
       
    @Parameters   
    public static Collection prepareData(){  //必须为public static的 返回值必须是Collection类型的
 
        Object [][] object = {{1,2,3},{4,5,9}};  //测试数据
        return Arrays.asList(object);  
    }  
      
 
    public AddTest(int para1,int para2,int expected){  
        this.para1 = para1;  
        this.para2 = para2;  
        this.expected = expected;  
    }  
 
    
    
    
    
    @Test  
    public void test(){  
        Add add = new Add();  
        int result = add.add(para1, para2);  
        assertEquals(expected,result);  
    }  
}


```

import java.util.Arrays;

/**
 * Created by Im on 2017/8/11.
 * 冒泡排序:两个for循环嵌套 外层循环整个list 内层循环从外层+1开始循环做比 大的后移 可能有list为空的情况,list中元素相等的情况
 */
public class Bubble_sort{
    public static void main(String[] args){
        int li[] = {3, 2, 4, 7, 4, 1, 9, 0};
        for (int i = 0; i < li.length -1; i++){    //
            for(int j = i + 1 ;j < li.length - 1; j++){
                //
                if(li[i] >= li[j + 1]){
                    //
                    int temp = li[i];
                    li[i] = li[j];
                    li[j] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(li));
    }
}
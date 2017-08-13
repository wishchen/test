package test;

import java.util.Arrays;

/**
 * Created by Im on 2017/8/13.
 */
public class Select_Sort {
    public  static void main(String args[]){
        int score[] = {3, 2, 4, 7, 4, 1, 9, 0};

        for(int i = 0; i <= score.length - 1; i ++){
            int temp = i;
            int ttemp = score[i];
            for (int j = i + 1; j < score.length; j ++){
                if (ttemp >= score[j]){
                    temp = j;
                    ttemp = score[j];
                }
            }
            if (i != temp){
                int scoreTemp = score[temp];
                score[temp] = score[i];
                score[i] = scoreTemp;
            }
        }

        System.out.println(Arrays.toString(score));

    }
}

import java.io.*;
import java.util.*;
/**
 * Already solved in python. Solving again in Java to prepare for classes next semester.
 *
 * @dtmulc
 * @12.01.18
 */
public class aoc_2018_1
{
    public static void main(String[] args)throws Exception{
        File file = new File("../p1.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String line;
        int count = 0;
        int sum = 0;
        String data[] = new String[how_long()];
        int checked[];
        // checked[0] = 0;
        while ((line = br.readLine()) != null){
           data[count] = line;
           count ++;
        }
        for (int i = 0; i < (data.length); i++){
            sum += Integer.parseInt(data[i]);
            // if (IntSteam.of(checked).anyMatch(x -> x == sum)){
                // System.out.out.println(sum);
            // }
            // else{
                
            // }
        }
        // for(int i = 0; i < br.length(); i++){
            // String lines[i] = br.readLine();
        // }
        System.out.println(sum);
           
        
        
    }
    public static int how_long()throws Exception{
       File infil = new File("../p1.txt");
       BufferedReader br = new BufferedReader(new FileReader(infil));
       int count = 0;
       String line;
       while ((line= br.readLine()) != null){
           count ++;
       }
       return count;
    }
}

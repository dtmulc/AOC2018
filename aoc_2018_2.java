import java.io.*;
import java.util.*;
/**
 * Write a description of class aoc_2018_2 here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class aoc_2018_2
{
    public static void main(String[] args)throws Exception{
        File file = new File("../p2.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));
        String line;
        int count = 0;
        int sum = 0;
        int twos = 0;
        int threes = 0;
        String data[] = new String[how_long()];
        while ((line = br.readLine()) != null){
           data[count] = line;
           count ++;
        }
        for (int i = 0; i < data.length; i ++){
            boolean has_twos = false;
            boolean has_three = false;
            String this_line = data[i];
            Map<Character,Integer> seen = new HashMap<Character, Integer>();
            for (int j = 0; j < this_line.length(); i ++){
                char curr_char = this_line.charAt(j);
                if(seen.containsKey(curr_char)){
                    seen.put(curr_char, seen.get(curr_char) + 1);
                }
                else{
                    seen.put(curr_char, 1);
                }
            }
            if (seen.values().stream().anyMatch(x -> x == 2)){ has_twos = true;}
            if (seen.values().stream().anyMatch(x -> x == 3)){ has_three = true;}
            if (has_twos) { twos ++; }
            if (has_three) { threes ++; }
        }
        System.out.print(twos * threes);
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


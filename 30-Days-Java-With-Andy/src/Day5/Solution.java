package Day5;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
 public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();

        
    

        while(scan.hasNext()){
            String S = scan.next();
            StringBuilder evenString = new StringBuilder();
            StringBuilder oddString = new StringBuilder();

        for (int i = 0; i < S.length(); i++){
            if (i % 2 == 0){
               evenString.append(S.charAt(i));
            } else {
                oddString.append(S.charAt(i));
            }
        }
        System.out.println(evenString.toString() + ' ' + oddString.toString());

        }
        


        scan.close();
    }
}

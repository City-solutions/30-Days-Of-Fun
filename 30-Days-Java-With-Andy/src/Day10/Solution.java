package Day10;

import java.io.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        
        bufferedReader.close();
        
         String bin = Integer.toBinaryString(n);
        int count=0;
        int max = 0;
        for(int i = 0; i < bin.length(); i++){
            if(bin.charAt(i) == '0'){
                count = 0;
            }
            else{
                count++;
                max = Math.max(count, max);
            }
            
        }
        
        System.out.println(max);
        
    }
}

package Day8;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Map<String, Integer> mynumMap = new HashMap<>();        
        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            mynumMap.put(name, phone);
        }
        while(in.hasNext()){
            String s = in.next();
            // Write code here
            if(mynumMap.containsKey(s)){
                System.out.println(s+"="+mynumMap.get(s));
            }
            else{
                System.out.println("Not found");
            }
        }
        in.close();
    }
}
package Day9;

import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int resultFactorial = Result.factorial(n);
        System.out.println(resultFactorial);
        in.close();
    }
}
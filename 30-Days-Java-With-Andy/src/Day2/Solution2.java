package Day2;

import java.util.Scanner;

public class Solution2 {

    public static void main(String[] args) {

        int i = 4;
        double d = 4.0;
        String s = "HackerRank ";
        Scanner scanner = new Scanner(System.in); // get input from STDIN

        int i2 = scanner.nextInt(); // get int from STDIN
        double d2 = scanner.nextDouble(); // get double from STDIN
        scanner.nextLine(); // consume the newline character
        String s2 = scanner.next(); // get String from STDIN


        System.out.println(i + i2);
        System.out.println(d + d2);
        s2 = scanner.nextLine(); // I almost couldn't figure out why this line is needed.
        System.out.println(s + s2);

        scanner.close(); 


    }

}

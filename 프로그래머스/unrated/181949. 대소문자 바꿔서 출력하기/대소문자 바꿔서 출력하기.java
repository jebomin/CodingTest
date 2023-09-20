import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        String rs = "";
        
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            
            if (Character.isUpperCase(c)) {
                rs += Character.toLowerCase(c);
            } else {
                rs += Character.toUpperCase(c);
            }
        }
        System.out.println(rs);
    }
}
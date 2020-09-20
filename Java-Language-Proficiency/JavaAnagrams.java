import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        a=a.toLowerCase();
        b=b.toLowerCase();
        if(a.length()!=b.length())
            return false;
        else
        {
            int i=0;
            while(true)
            {
                int n=a.indexOf(b.charAt(i++));
                if(n==-1)
                    return false;
                else if(n==a.length()-1)
                     a=a.substring(0,n);
                else
                    a=a.substring(0,n)+a.substring(n+1);
                if(i==b.length())
                    return true;
            }
        }
        // Complete the function
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}

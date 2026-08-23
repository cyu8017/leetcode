// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution {
    public String strWithout3a3b(int a, int b) {
        StringBuilder ans = new StringBuilder();
        while (a > 0 || b > 0) {
            boolean writeA;
            int len = ans.length();
            if (len >= 2 && ans.charAt(len - 1) == ans.charAt(len - 2))
                writeA = ans.charAt(len - 1) == 'b';
            else
                writeA = a >= b;
            if (writeA) { ans.append('a'); a--; }
            else { ans.append('b'); b--; }
        }
        return ans.toString();
    }
}

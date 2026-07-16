// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

class Solution {
    public int numDecodings(String s) {
        if (s == null || s.isEmpty() || s.charAt(0) == '0') {
            return 0;
        }

        int prev2 = 1;
        int prev1 = 1;

        for (int i = 1; i < s.length(); i++) {
            int current = 0;
            if (s.charAt(i) != '0') {
                current += prev1;
            }
            int two = Integer.parseInt(s.substring(i - 1, i + 1));
            if (two >= 10 && two <= 26) {
                current += prev2;
            }
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}

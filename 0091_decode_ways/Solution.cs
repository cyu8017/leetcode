// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

public class Solution {
    public int NumDecodings(string s) {
        if (string.IsNullOrEmpty(s) || s[0] == '0') {
            return 0;
        }

        int prev2 = 1;
        int prev1 = 1;

        for (int i = 1; i < s.Length; i++) {
            int current = 0;
            if (s[i] != '0') {
                current += prev1;
            }
            int two = int.Parse(s.Substring(i - 1, 2));
            if (two >= 10 && two <= 26) {
                current += prev2;
            }
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
}

// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

public class Solution {
    private static int One(char ch) {
        if (ch == '*') return 9;
        if (ch == '0') return 0;
        return 1;
    }

    private static int Two(char a, char b) {
        if (a == '*' && b == '*') return 15;
        if (a == '*') return b <= '6' ? 2 : 1;
        if (b == '*') {
            if (a == '1') return 9;
            if (a == '2') return 6;
            return 0;
        }
        int value = (a - '0') * 10 + (b - '0');
        return value >= 10 && value <= 26 ? 1 : 0;
    }

    public int NumDecodings(string s) {
        const int mod = 1000000007;
        long prev2 = 1;
        long prev1 = One(s[0]);
        for (int i = 1; i < s.Length; ++i) {
            long cur = (One(s[i]) * prev1 + Two(s[i - 1], s[i]) * prev2) % mod;
            prev2 = prev1;
            prev1 = cur;
        }
        return (int)prev1;
    }
}

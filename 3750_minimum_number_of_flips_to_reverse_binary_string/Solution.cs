// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

using System;
using System.Text;

public class Solution {
    public int MinimumFlips(int n) {
        string s;
        long x = n;
        if (x == 0) s = "0";
        else {
            var sb = new StringBuilder();
            while (x > 0) {
                sb.Append((char)('0' + (x & 1)));
                x >>= 1;
            }
            char[] arr = sb.ToString().ToCharArray();
            Array.Reverse(arr);
            s = new string(arr);
        }
        int m = s.Length, cnt = 0;
        for (int i = 0; i < m / 2; i++) {
            if (s[i] != s[m - i - 1]) cnt++;
        }
        return cnt * 2;
    }
}

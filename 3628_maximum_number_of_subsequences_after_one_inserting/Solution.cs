// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

using System;

public class Solution {
    public long NumOfSubsequences(string s) {
        long Calc(string t) {
            long cnt = 0, a = 0;
            foreach (char c in s) {
                if (c == t[1]) cnt += a;
                if (c == t[0]) a++;
            }
            return cnt;
        }
        long l = 0, r = 0;
        foreach (char c in s)
            if (c == 'T') r++;
        long ans = 0, mx = 0;
        foreach (char c in s) {
            if (c == 'T') r--;
            if (c == 'C') ans += l * r;
            if (c == 'L') l++;
            mx = Math.Max(mx, l * r);
        }
        mx = Math.Max(mx, Math.Max(Calc("LC"), Calc("CT")));
        return ans + mx;
    }
}

// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

using System.Collections.Generic;

public class Solution {
    public long FixedRatio(string s, int num1, int num2) {
        var pref = new Dictionary<long, int>();
        pref[0] = 1;
        int zeros = 0, ones = 0;
        long ans = 0;
        foreach (char c in s) {
            if (c == '0') zeros++;
            else ones++;
            long key = 1L * zeros * num2 - 1L * ones * num1;
            if (pref.ContainsKey(key)) ans += pref[key];
            if (!pref.ContainsKey(key)) pref[key] = 0;
            pref[key]++;
        }
        return ans;
    }
}

// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSameLengthRuns(string s) {
        var cnt = new Dictionary<int, int>();
        int n = s.Length, ans = 0;
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && s[j] == s[i]) j++;
            int m = j - i;
            if (!cnt.ContainsKey(m)) cnt[m] = 0;
            cnt[m]++;
            ans = Math.Max(ans, cnt[m]);
            i = j;
        }
        return ans;
    }
}

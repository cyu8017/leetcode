// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestBalanced(string s) {
        int cnt0 = 0;
        foreach (char c in s) if (c == '0') cnt0++;
        int cnt1 = s.Length - cnt0;
        var pos = new Dictionary<int, List<int>>();
        pos[0] = new List<int> { -1 };
        int ans = 0, pre = 0;
        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '1') pre++;
            else pre--;
            if (!pos.ContainsKey(pre)) pos[pre] = new List<int>();
            pos[pre].Add(i);
            ans = Math.Max(ans, i - pos[pre][0]);
            if (pos.ContainsKey(pre - 2)) {
                var p = pos[pre - 2];
                if ((i - p[0] - 2) / 2 < cnt0) ans = Math.Max(ans, i - p[0]);
                else if (p.Count > 1) ans = Math.Max(ans, i - p[1]);
            }
            if (pos.ContainsKey(pre + 2)) {
                var p = pos[pre + 2];
                if ((i - p[0] - 2) / 2 < cnt1) ans = Math.Max(ans, i - p[0]);
                else if (p.Count > 1) ans = Math.Max(ans, i - p[1]);
            }
        }
        return ans;
    }
}

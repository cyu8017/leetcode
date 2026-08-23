// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

using System.Collections.Generic;

public class Solution {
    public int PrefixConnected(string[] words, int k) {
        var cnt = new Dictionary<string, int>();
        foreach (var w in words) {
            if (w.Length >= k) {
                string p = w.Substring(0, k);
                if (!cnt.ContainsKey(p)) cnt[p] = 0;
                cnt[p]++;
            }
        }
        int ans = 0;
        foreach (var v in cnt.Values) if (v > 1) ans++;
        return ans;
    }
}

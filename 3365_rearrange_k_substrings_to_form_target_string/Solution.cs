// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

using System.Collections.Generic;

public class Solution {
    public bool IsPossibleToRearrange(string s, string t, int k) {
        int n = s.Length;
        int sz = n / k;
        var cnt = new Dictionary<string, int>();
        for (int i = 0; i < n; i += sz) {
            string a = s.Substring(i, sz), b = t.Substring(i, sz);
            if (!cnt.ContainsKey(a)) cnt[a] = 0;
            cnt[a]++;
            if (!cnt.ContainsKey(b)) cnt[b] = 0;
            cnt[b]--;
        }
        foreach (var v in cnt.Values) if (v != 0) return false;
        return true;
    }
}

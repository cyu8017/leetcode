// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string MajorityFrequencyGroup(string s) {
        int[] cnt = new int[26];
        foreach (char c in s) cnt[c - 'a']++;
        var f = new Dictionary<int, StringBuilder>();
        for (int i = 0; i < 26; i++) {
            if (cnt[i] > 0) {
                if (!f.ContainsKey(cnt[i])) f[cnt[i]] = new StringBuilder();
                f[cnt[i]].Append((char)('a' + i));
            }
        }
        int mx = 0, mv = 0;
        string ans = "";
        foreach (var kv in f) {
            int v = kv.Key;
            string cs = kv.Value.ToString();
            if (cs.Length > mx || (cs.Length == mx && v > mv)) {
                mx = cs.Length;
                mv = v;
                ans = cs;
            }
        }
        return ans;
    }
}

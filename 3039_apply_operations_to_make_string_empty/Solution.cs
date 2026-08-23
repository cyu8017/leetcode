// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

using System;
using System.Text;

public class Solution {
    public string LastNonEmptyString(string s) {
        int[] cnt = new int[26], last = new int[26];
        int mx = 0;
        for (int i = 0; i < s.Length; i++) {
            int c = s[i] - 'a';
            cnt[c]++;
            last[c] = i;
            mx = Math.Max(mx, cnt[c]);
        }
        var ans = new StringBuilder();
        for (int i = 0; i < s.Length; i++) {
            int c = s[i] - 'a';
            if (cnt[c] == mx && last[c] == i) ans.Append(s[i]);
        }
        return ans.ToString();
    }
}

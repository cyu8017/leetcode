// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string RemoveSubstring(string s, int k) {
        var stk = new List<(char ch, int count)>();
        foreach (char c in s) {
            if (stk.Count > 0 && stk[stk.Count - 1].ch == c) {
                var top = stk[stk.Count - 1];
                stk[stk.Count - 1] = (top.ch, top.count + 1);
            } else stk.Add((c, 1));
            if (c == ')' && stk.Count > 1) {
                var top = stk[stk.Count - 1];
                var prev = stk[stk.Count - 2];
                if (top.count == k && prev.count >= k) {
                    stk.RemoveAt(stk.Count - 1);
                    prev = (prev.ch, prev.count - k);
                    if (prev.count == 0) stk.RemoveAt(stk.Count - 1);
                    else stk[stk.Count - 1] = prev;
                }
            }
        }
        var res = new StringBuilder();
        foreach (var (ch, count) in stk) res.Append(ch, count);
        return res.ToString();
    }
}

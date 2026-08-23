// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

using System;

public class Solution {
    public string MinimumString(string a, string b, string c) {
        string Merge(string x, string y) {
            if (x.Contains(y)) return x;
            string best = x + y;
            int n = Math.Min(x.Length, y.Length);
            for (int i = n; i > 0; i--) {
                if (x.Substring(x.Length - i) == y.Substring(0, i)) {
                    string cand = x + y.Substring(i);
                    if (cand.Length < best.Length || (cand.Length == best.Length && string.CompareOrdinal(cand, best) < 0))
                        best = cand;
                    break;
                }
            }
            return best;
        }
        string[][] perms = {
            new[]{a,b,c}, new[]{a,c,b}, new[]{b,a,c}, new[]{b,c,a}, new[]{c,a,b}, new[]{c,b,a}
        };
        string ans = "";
        foreach (var p in perms) {
            string cur = Merge(Merge(p[0], p[1]), p[2]);
            if (ans.Length == 0 || cur.Length < ans.Length || (cur.Length == ans.Length && string.CompareOrdinal(cur, ans) < 0))
                ans = cur;
        }
        return ans;
    }
}

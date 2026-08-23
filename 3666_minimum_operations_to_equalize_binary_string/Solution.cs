// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinOperations(string s, int k) {
        int n = s.Length;
        var ts = new SortedSet<int>[2];
        ts[0] = new SortedSet<int>();
        ts[1] = new SortedSet<int>();
        for (int i = 0; i <= n; i++) ts[i % 2].Add(i);
        int cnt0 = s.Count(c => c == '0');
        ts[cnt0 % 2].Remove(cnt0);
        var q = new List<int> { cnt0 };
        int ans = 0;
        while (q.Count > 0) {
            var nq = new List<int>();
            foreach (int cur in q) {
                if (cur == 0) return ans;
                int l = cur + k - 2 * Math.Min(cur, k);
                int r = cur + k - 2 * Math.Max(k - n + cur, 0);
                var t = ts[l % 2];
                var toRemove = t.GetViewBetween(l, r).ToList();
                foreach (int v in toRemove) {
                    nq.Add(v);
                    t.Remove(v);
                }
            }
            q = nq;
            ans++;
        }
        return -1;
    }
}

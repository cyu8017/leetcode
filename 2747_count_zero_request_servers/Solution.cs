// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountServers(int n, int[][] logs, int x, int[] queries) {
        Array.Sort(logs, (a, b) => a[1].CompareTo(b[1]));
        var qs = new (int t, int i)[queries.Length];
        for (int i = 0; i < queries.Length; i++) qs[i] = (queries[i], i);
        Array.Sort(qs, (a, b) => a.t.CompareTo(b.t));
        int[] ans = new int[queries.Length];
        var cnt = new Dictionary<int, int>();
        int active = 0, l = 0, r = 0;
        foreach (var q in qs) {
            while (r < logs.Length && logs[r][1] <= q.t) {
                int id = logs[r][0];
                if (!cnt.ContainsKey(id)) cnt[id] = 0;
                if (cnt[id] == 0) active++;
                cnt[id]++;
                r++;
            }
            while (l < r && logs[l][1] < q.t - x) {
                int id = logs[l][0];
                cnt[id]--;
                if (cnt[id] == 0) active--;
                l++;
            }
            ans[q.i] = n - active;
        }
        return ans;
    }
}

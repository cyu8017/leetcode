// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxRequests(int[][] requests, int k, int window) {
        var g = new Dictionary<int, List<int>>();
        foreach (var r in requests) {
            if (!g.ContainsKey(r[0])) g[r[0]] = new List<int>();
            g[r[0]].Add(r[1]);
        }
        int ans = requests.Length;
        foreach (var ts in g.Values) {
            ts.Sort();
            var kept = new List<int>();
            foreach (int t in ts) {
                while (kept.Count > 0 && t - kept[0] > window) kept.RemoveAt(0);
                if (kept.Count < k) kept.Add(t);
                else ans--;
            }
        }
        return ans;
    }
}

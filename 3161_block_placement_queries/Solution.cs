// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

using System;
using System.Collections.Generic;

public class Solution {
    class FenwickMax {
        int[] vals;
        public FenwickMax(int n) { vals = new int[n + 1]; }
        public void Maximize(int i, int val) {
            for (; i < vals.Length; i += i & -i)
                vals[i] = Math.Max(vals[i], val);
        }
        public int Get(int i) {
            int res = 0;
            for (; i > 0; i -= i & -i) res = Math.Max(res, vals[i]);
            return res;
        }
    }

    public bool[] GetResults(int[][] queries) {
        int n = queries.Length * 3;
        if (n > 50000) n = 50000;
        var tree = new FenwickMax(n + 1);
        var obs = new List<int> { 0, n };
        foreach (var q in queries) {
            if (q[0] == 1) {
                int x = q[1];
                int idx = LowerBound(obs, x);
                if (idx == obs.Count || obs[idx] != x) obs.Insert(idx, x);
            }
        }
        for (int i = 0; i + 1 < obs.Count; i++) {
            tree.Maximize(obs[i + 1], obs[i + 1] - obs[i]);
        }
        var ans = new List<bool>();
        for (int i = queries.Length - 1; i >= 0; i--) {
            int typ = queries[i][0], x = queries[i][1];
            if (typ == 1) {
                int j = LowerBound(obs, x);
                int prev = obs[j - 1], next = obs[j + 1];
                obs.RemoveAt(j);
                tree.Maximize(next, next - prev);
            } else {
                int sz = queries[i][2];
                int j = LowerBound(obs, x + 1) - 1;
                int prev = obs[j];
                ans.Add(tree.Get(prev) >= sz || x - prev >= sz);
            }
        }
        ans.Reverse();
        return ans.ToArray();
    }

    static int LowerBound(List<int> a, int x) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

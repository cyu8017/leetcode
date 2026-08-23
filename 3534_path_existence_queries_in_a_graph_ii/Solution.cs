// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] PathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        var pairs = new (int val, int idx)[n];
        for (int i = 0; i < n; i++) pairs[i] = (nums[i], i);
        Array.Sort(pairs);
        int m = 20;
        int[][] f = new int[n][];
        for (int i = 0; i < n; i++) f[i] = new int[m];
        int r = n - 1;
        for (int l = n - 1; l >= 0; l--) {
            while (pairs[r].val - pairs[l].val > maxDiff) r--;
            int i = pairs[l].idx, j = pairs[r].idx;
            f[i][0] = j;
            for (int k = 1; k < m; k++) f[i][k] = f[f[i][k - 1]][k - 1];
        }
        var ans = new List<int>();
        foreach (var q in queries) {
            int i = q[0], j = q[1];
            if (nums[i] > nums[j]) { int tmp = i; i = j; j = tmp; }
            if (i == j) { ans.Add(0); continue; }
            if (nums[i] == nums[j]) { ans.Add(1); continue; }
            int d = 0;
            for (int k = m - 1; k >= 0; k--) {
                if (nums[f[i][k]] < nums[j]) {
                    d |= 1 << k;
                    i = f[i][k];
                }
            }
            if (nums[f[i][0]] < nums[j]) ans.Add(-1);
            else ans.Add(d + 1);
        }
        return ans.ToArray();
    }
}

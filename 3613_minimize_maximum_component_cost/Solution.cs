// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

using System;

public class Solution {
    public int MinCost(int n, int[][] edges, int k) {
        int[] p = new int[n];
        for (int i = 0; i < n; i++) p[i] = i;
        int Find(int x) {
            return p[x] == x ? x : (p[x] = Find(p[x]));
        }
        if (k == n) return 0;
        Array.Sort(edges, (a, b) => a[2].CompareTo(b[2]));
        int cnt = n;
        foreach (var e in edges) {
            int pu = Find(e[0]), pv = Find(e[1]);
            if (pu != pv) {
                p[pu] = pv;
                if (--cnt <= k) return e[2];
            }
        }
        return 0;
    }
}

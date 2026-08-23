// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSumDistinctTriplet(int[] x, int[] y) {
        int n = x.Length;
        var arr = new (int a, int b)[n];
        for (int i = 0; i < n; i++) arr[i] = (x[i], y[i]);
        Array.Sort(arr, (p, q) => q.b.CompareTo(p.b));
        int ans = 0;
        var vis = new HashSet<int>();
        for (int i = 0; i < n; i++) {
            int a = arr[i].a, b = arr[i].b;
            if (!vis.Contains(a)) {
                vis.Add(a);
                ans += b;
                if (vis.Count == 3) return ans;
            }
        }
        return -1;
    }
}

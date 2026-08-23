// LeetCode 3796 - Find Maximum Value in a Constrained Sequence
// https://leetcode.com/problems/find-maximum-value-in-a-constrained-sequence/

using System;

public class Solution {
    public int MaxValue(int n, int[][] restrictions, int[] diff) {
        const int INF = int.MaxValue / 4;
        int[] bound = new int[n];
        for (int i = 0; i < n; i++) bound[i] = INF;
        bound[0] = 0;
        foreach (var r in restrictions) bound[r[0]] = r[1];
        for (int i = 1; i < n; i++) bound[i] = Math.Min(bound[i], bound[i - 1] + diff[i - 1]);
        for (int i = n - 2; i >= 0; i--) bound[i] = Math.Min(bound[i], bound[i + 1] + diff[i]);
        int ans = bound[0];
        for (int i = 1; i < n; i++) ans = Math.Max(ans, bound[i]);
        return ans;
    }
}

// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

using System;

public class Solution {
    public int MaxAbsValExpr(int[] arr1, int[] arr2) {
        int n = arr1.Length;
        int ans = 0;
        int[][] signs = { new[] { 1, 1 }, new[] { 1, -1 }, new[] { -1, 1 }, new[] { -1, -1 } };
        foreach (var pq in signs) {
            int best = pq[0] * arr1[0] + pq[1] * arr2[0];
            for (int i = 1; i < n; i++) {
                int cur = pq[0] * arr1[i] + pq[1] * arr2[i] + i;
                ans = Math.Max(ans, cur - best);
                best = Math.Min(best, cur);
            }
        }
        return ans;
    }
}

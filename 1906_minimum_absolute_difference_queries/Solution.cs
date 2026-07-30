// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

using System;

public class Solution {
    public int[] MinDifference(int[] nums, int[][] queries) {
        int n = nums.Length;
        var pref = new int[n + 1][];
        pref[0] = new int[101];
        for (int i = 0; i < n; i++) {
            pref[i + 1] = (int[])pref[i].Clone();
            pref[i + 1][nums[i]]++;
        }
        var ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int left = queries[qi][0], right = queries[qi][1];
            int prev = -1, best = int.MaxValue;
            for (int value = 1; value <= 100; value++) {
                if (pref[right + 1][value] - pref[left][value] > 0) {
                    if (prev != -1) best = Math.Min(best, value - prev);
                    prev = value;
                }
            }
            ans[qi] = best == int.MaxValue ? -1 : best;
        }
        return ans;
    }
}
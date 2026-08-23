// LeetCode 2448 - Minimum Cost to Make Array Equal
// https://leetcode.com/problems/minimum-cost-to-make-array-equal/

using System;

public class Solution {
    public long MinCost(int[] nums, int[] cost) {
        int n = nums.Length;
        int[] idx = new int[n];
        for (int i = 0; i < n; i++) idx[i] = i;
        Array.Sort(idx, (a, b) => nums[a].CompareTo(nums[b]));
        long totalCost = 0;
        foreach (int c in cost) totalCost += c;
        long pref = 0;
        int median = 0;
        foreach (int i in idx) {
            pref += cost[i];
            if (pref * 2 >= totalCost) {
                median = nums[i];
                break;
            }
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long diff = nums[i] - median;
            if (diff < 0) diff = -diff;
            ans += diff * cost[i];
        }
        return ans;
    }
}

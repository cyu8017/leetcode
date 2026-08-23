// LeetCode 3139 - Minimum Cost to Equalize Array
// https://leetcode.com/problems/minimum-cost-to-equalize-array/

using System;

public class Solution {
    public int MinCostToEqualizeArray(int[] nums, int cost1, int cost2) {
        const int Mod = 1000000007;
        int n = nums.Length;
        int minNum = nums[0], maxNum = nums[0];
        long sum = 0;
        foreach (int v in nums) {
            minNum = Math.Min(minNum, v);
            maxNum = Math.Max(maxNum, v);
            sum += v;
        }
        if (cost1 * 2L <= cost2 || n < 3) {
            long totalGap = 1L * maxNum * n - sum;
            return (int)(1L * cost1 * totalGap % Mod);
        }
        long ans = long.MaxValue;
        for (int target = maxNum; target < 2 * maxNum; target++) {
            int maxGap = target - minNum;
            long totalGap = 1L * target * n - sum;
            long pairs = totalGap / 2;
            long alt = totalGap - maxGap;
            if (alt < pairs) pairs = alt;
            long cost = 1L * cost1 * (totalGap - 2 * pairs) + 1L * cost2 * pairs;
            ans = Math.Min(ans, cost);
        }
        return (int)(ans % Mod);
    }
}

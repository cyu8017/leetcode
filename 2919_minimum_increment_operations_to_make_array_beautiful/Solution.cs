// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

using System;

public class Solution {
    public long MinIncrementOperations(int[] nums, int k) {
        long dp0 = 0, dp1 = 0, dp2 = 0;
        foreach (int v in nums) {
            long cost = v < k ? (k - v) : 0;
            long nd0 = cost + Math.Min(dp0, Math.Min(dp1, dp2));
            dp0 = dp1; dp1 = dp2; dp2 = nd0;
        }
        return Math.Min(dp0, Math.Min(dp1, dp2));
    }
}

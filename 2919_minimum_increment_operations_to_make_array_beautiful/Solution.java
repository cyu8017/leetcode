// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution {
    public long minIncrementOperations(int[] nums, int k) {
        long dp0 = 0, dp1 = 0, dp2 = 0;
        for (int v : nums) {
            long cost = v < k ? (k - v) : 0;
            long nd0 = cost + Math.min(dp0, Math.min(dp1, dp2));
            dp0 = dp1;
            dp1 = dp2;
            dp2 = nd0;
        }
        return Math.min(dp0, Math.min(dp1, dp2));
    }
}

// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution {
    fun minIncrementOperations(nums: IntArray, k: Int): Long {
        var dp0 = 0
        var dp1 = 0
        var dp2 = 0
        for (v in nums) {
            var cost = if (v < k) (k - v) else 0
            var nd0 = cost + minOf(dp0, minOf(dp1, dp2))
            dp0 = dp1
            dp1 = dp2
            dp2 = nd0
        }
        return minOf(dp0, minOf(dp1, dp2))
    }
}

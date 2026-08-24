// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

class Solution {
    func minIncrementOperations(_ nums: [Int], _ k: Int) -> Int {
        var dp0 = 0, dp1 = 0, dp2 = 0
        for v in nums {
            let cost = v < k ? k - v : 0
            let nd0 = cost + min(dp0, min(dp1, dp2))
            dp0 = dp1
            dp1 = dp2
            dp2 = nd0
        }
        return min(dp0, min(dp1, dp2))
    }
}

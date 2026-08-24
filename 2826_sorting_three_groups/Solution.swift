// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        let INF = 1 << 30
        var dp = Array(repeating: Array(repeating: INF, count: 4), count: n + 1)
        dp[0][1] = 0; dp[0][2] = 0; dp[0][3] = 0
        for i in 1...n {
            let v = nums[i - 1]
            for g in 1...3 {
                let cost = v != g ? 1 : 0
                for prev in 1...g {
                    dp[i][g] = min(dp[i][g], dp[i - 1][prev] + cost)
                }
            }
        }
        return min(dp[n][1], dp[n][2], dp[n][3])
    }
}

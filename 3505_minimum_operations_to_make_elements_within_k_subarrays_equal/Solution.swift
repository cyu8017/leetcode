// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

class Solution {
    func minOperations(_ nums: [Int], _ x: Int, _ k: Int) -> Int {
        let n = nums.count
        var minOps = Array(repeating: 0, count: n - x + 1)
        for i in 0...(n - x) {
            var w = Array(nums[i..<(i + x)])
            w.sort()
            let med = w[(x - 1) / 2]
            var ops = 0
            for v in w { ops += abs(v - med) }
            minOps[i] = ops
        }
        let Inf = Int.max / 4
        var dp = Array(repeating: Array(repeating: Inf, count: k + 1), count: n + 1)
        dp[n][0] = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in 0...k {
                dp[i][j] = dp[i + 1][j]
                if j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j] {
                    dp[i][j] = minOps[i] + dp[i + x][j - 1]
                }
            }
        }
        return dp[0][k]
    }
}

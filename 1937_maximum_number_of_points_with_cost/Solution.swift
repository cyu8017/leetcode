// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution {
    func maxPoints(_ points: [[Int]]) -> Int {
        let m = points.count, n = points[0].count
        var dp = points[0]
        for r in 1..<m {
            var left = Array(repeating: 0, count: n)
            var right = Array(repeating: 0, count: n)
            left[0] = dp[0]
            for c in 1..<n { left[c] = max(left[c - 1] - 1, dp[c]) }
            right[n - 1] = dp[n - 1]
            for c in stride(from: n - 2, through: 0, by: -1) {
                right[c] = max(right[c + 1] - 1, dp[c])
            }
            dp = (0..<n).map { points[r][$0] + max(left[$0], right[$0]) }
        }
        return dp.max()!
    }
}

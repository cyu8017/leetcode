// LeetCode 1547 - Minimum Cost to Cut a Stick
// https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

class Solution {
    func minCost(_ n: Int, _ cuts: [Int]) -> Int {
        let points = [0] + cuts.sorted() + [n]
        let size = points.count
        var dp = Array(repeating: Array(repeating: 0, count: size), count: size)
        for width in 2..<size {
            for left in 0..<(size - width) {
                let right = left + width
                var best = Int.max
                for mid in (left + 1)..<right {
                    best = min(best, dp[left][mid] + dp[mid][right])
                }
                if best == Int.max { best = 0 }
                if right > left + 1 {
                    best += points[right] - points[left]
                }
                dp[left][right] = best
            }
        }
        return dp[0][size - 1]
    }
}

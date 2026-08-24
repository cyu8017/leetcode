// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

class Solution {
    func orderOfLargestPlusSign(_ n: Int, _ mines: [[Int]]) -> Int {
        var banned = Set<Int>()
        for m in mines { banned.insert(m[0] * n + m[1]) }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        var ans = 0
        for r in 0..<n {
            var count = 0
            for c in 0..<n {
                count = banned.contains(r * n + c) ? 0 : count + 1
                dp[r][c] = count
            }
            count = 0
            for c in stride(from: n - 1, through: 0, by: -1) {
                count = banned.contains(r * n + c) ? 0 : count + 1
                dp[r][c] = min(dp[r][c], count)
            }
        }
        for c in 0..<n {
            var count = 0
            for r in 0..<n {
                count = banned.contains(r * n + c) ? 0 : count + 1
                dp[r][c] = min(dp[r][c], count)
            }
            count = 0
            for r in stride(from: n - 1, through: 0, by: -1) {
                count = banned.contains(r * n + c) ? 0 : count + 1
                dp[r][c] = min(dp[r][c], count)
                ans = max(ans, dp[r][c])
            }
        }
        return ans
    }
}

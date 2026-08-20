// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

class Solution {
    func minFallingPathSum(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var dp = grid[0]
        for r in 1..<n {
            var first = -1, second = -1
            for i in 0..<n {
                if first == -1 || dp[i] < dp[first] {
                    second = first; first = i
                } else if second == -1 || dp[i] < dp[second] {
                    second = i
                }
            }
            var next = [Int](repeating: 0, count: n)
            for i in 0..<n {
                next[i] = grid[r][i] + (i == first ? dp[second] : dp[first])
            }
            dp = next
        }
        return dp.min()!
    }
}

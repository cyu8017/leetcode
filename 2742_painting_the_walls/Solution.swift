// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/

class Solution {
    func paintWalls(_ cost: [Int], _ time: [Int]) -> Int {
        let n = cost.count
        let INF = Int.max / 4
        var dp = Array(repeating: INF, count: n + 1)
        dp[0] = 0
        for i in 0..<n {
            for j in stride(from: n, through: 0, by: -1) {
                let nj = min(n, j + time[i] + 1)
                if dp[j] + cost[i] < dp[nj] { dp[nj] = dp[j] + cost[i] }
            }
        }
        return dp[n]
    }
}

// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

class Solution {
    func minCost(_ n: Int, _ cost: [[Int]]) -> Int {
        let inf = 1 << 60
        let m = n / 2
        var dp = Array(repeating: Array(repeating: 0, count: 3), count: 3)
        for a in 0..<3 {
            for b in 0..<3 {
                dp[a][b] = a == b ? inf : cost[0][a] + cost[n - 1][b]
            }
        }
        if m > 1 {
            for i in 1..<m {
                var ndp = Array(repeating: Array(repeating: inf, count: 3), count: 3)
                for pa in 0..<3 {
                    for pb in 0..<3 {
                        if dp[pa][pb] >= inf { continue }
                        for a in 0..<3 where a != pa {
                            for b in 0..<3 where b != pb && a != b {
                                let v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
                                if v < ndp[a][b] { ndp[a][b] = v }
                            }
                        }
                    }
                }
                dp = ndp
            }
        }
        var ans = inf
        for a in 0..<3 {
            for b in 0..<3 where dp[a][b] < ans { ans = dp[a][b] }
        }
        return ans
    }
}

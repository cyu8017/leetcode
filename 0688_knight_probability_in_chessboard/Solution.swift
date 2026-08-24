// LeetCode 0688 - Knight Probability in Chessboard
// https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution {
    func knightProbability(_ n: Int, _ k: Int, _ row: Int, _ column: Int) -> Double {
        let dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        var dp = Array(repeating: Array(repeating: 0.0, count: n), count: n)
        dp[row][column] = 1.0
        if k == 0 { return 1.0 }
        for _ in 0..<k {
            var nxt = Array(repeating: Array(repeating: 0.0, count: n), count: n)
            for r in 0..<n {
                for c in 0..<n where dp[r][c] > 0 {
                    for (dr, dc) in dirs {
                        let nr = r + dr, nc = c + dc
                        if nr >= 0 && nr < n && nc >= 0 && nc < n {
                            nxt[nr][nc] += dp[r][c] / 8.0
                        }
                    }
                }
            }
            dp = nxt
        }
        return dp.flatMap { $0 }.reduce(0, +)
    }
}

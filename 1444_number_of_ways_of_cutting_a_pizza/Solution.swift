// LeetCode 1444 - Number of Ways of Cutting a Pizza
// https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

class Solution {
    func ways(_ pizza: [String], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let rows = pizza.count, cols = pizza[0].count
        let grid = pizza.map { Array($0) }
        var apples = Array(repeating: Array(repeating: 0, count: cols + 1), count: rows + 1)
        for r in stride(from: rows - 1, through: 0, by: -1) {
            for c in stride(from: cols - 1, through: 0, by: -1) {
                apples[r][c] = (grid[r][c] == "A" ? 1 : 0) + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
            }
        }
        var dp = (0..<rows).map { r in (0..<cols).map { c in apples[r][c] > 0 ? 1 : 0 } }
        for _ in 1..<k {
            var nxt = Array(repeating: Array(repeating: 0, count: cols), count: rows)
            for r in 0..<rows {
                for c in 0..<cols {
                    for nr in (r + 1)..<rows where apples[r][c] > apples[nr][c] {
                        nxt[r][c] = (nxt[r][c] + dp[nr][c]) % mod
                    }
                    for nc in (c + 1)..<cols where apples[r][c] > apples[r][nc] {
                        nxt[r][c] = (nxt[r][c] + dp[r][nc]) % mod
                    }
                }
            }
            dp = nxt
        }
        return dp[0][0]
    }
}

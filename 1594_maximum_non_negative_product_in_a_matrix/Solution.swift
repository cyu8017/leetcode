// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

class Solution {
    func maxProductPath(_ grid: [[Int]]) -> Int {
        let MOD = 1_000_000_007
        let m = grid.count, n = grid[0].count
        var high = Array(repeating: Array(repeating: 0, count: n), count: m)
        var low = Array(repeating: Array(repeating: 0, count: n), count: m)
        high[0][0] = grid[0][0]
        low[0][0] = grid[0][0]
        for r in 0..<m {
            for c in 0..<n {
                if r == 0 && c == 0 { continue }
                var values = [Int]()
                if r > 0 {
                    values.append(high[r - 1][c] * grid[r][c])
                    values.append(low[r - 1][c] * grid[r][c])
                }
                if c > 0 {
                    values.append(high[r][c - 1] * grid[r][c])
                    values.append(low[r][c - 1] * grid[r][c])
                }
                high[r][c] = values.max()!
                low[r][c] = values.min()!
            }
        }
        return high[m - 1][n - 1] >= 0 ? high[m - 1][n - 1] % MOD : -1
    }
}

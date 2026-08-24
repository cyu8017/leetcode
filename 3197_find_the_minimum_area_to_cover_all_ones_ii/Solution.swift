// LeetCode 3197 - Find the Minimum Area to Cover All Ones II
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/

class Solution {
    func minimumSum(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var ans = m * n
        if m >= 3 {
            for i1 in 0..<(m - 1) {
                for i2 in (i1 + 1)..<(m - 1) {
                    ans = min(ans, area(grid, 0, 0, i1, n - 1) + area(grid, i1 + 1, 0, i2, n - 1) + area(grid, i2 + 1, 0, m - 1, n - 1))
                }
            }
        }
        if n >= 3 {
            for j1 in 0..<(n - 1) {
                for j2 in (j1 + 1)..<(n - 1) {
                    ans = min(ans, area(grid, 0, 0, m - 1, j1) + area(grid, 0, j1 + 1, m - 1, j2) + area(grid, 0, j2 + 1, m - 1, n - 1))
                }
            }
        }
        if m >= 2 && n >= 2 {
            for i in 0..<(m - 1) {
                for j in 0..<(n - 1) {
                    ans = min(ans, area(grid, 0, 0, i, j) + area(grid, 0, j + 1, i, n - 1) + area(grid, i + 1, 0, m - 1, n - 1))
                    ans = min(ans, area(grid, 0, 0, i, n - 1) + area(grid, i + 1, 0, m - 1, j) + area(grid, i + 1, j + 1, m - 1, n - 1))
                    ans = min(ans, area(grid, 0, 0, i, j) + area(grid, i + 1, 0, m - 1, j) + area(grid, 0, j + 1, m - 1, n - 1))
                    ans = min(ans, area(grid, 0, 0, m - 1, j) + area(grid, 0, j + 1, i, n - 1) + area(grid, i + 1, j + 1, m - 1, n - 1))
                }
            }
        }
        return ans
    }

    private func area(_ grid: [[Int]], _ i1: Int, _ j1: Int, _ i2: Int, _ j2: Int) -> Int {
        let inf = Int.max / 4
        var x1 = inf, y1 = inf, x2 = -inf, y2 = -inf
        for i in i1...i2 {
            for j in j1...j2 where grid[i][j] == 1 {
                x1 = min(x1, i); y1 = min(y1, j)
                x2 = max(x2, i); y2 = max(y2, j)
            }
        }
        if x1 == inf { return 0 }
        return (x2 - x1 + 1) * (y2 - y1 + 1)
    }
}

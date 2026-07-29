// LeetCode 1020 - Number of Enclaves
// https://leetcode.com/problems/number-of-enclaves/

class Solution {
    func numEnclaves(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 1 { return }
            grid[r][c] = 0
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)
        }
        for i in 0..<m {
            dfs(i, 0); dfs(i, n - 1)
        }
        for j in 0..<n {
            dfs(0, j); dfs(m - 1, j)
        }
        return grid.reduce(0) { $0 + $1.reduce(0, +) }
    }
}

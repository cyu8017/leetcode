// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

class Solution {
    func closedIsland(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        func dfs(_ r: Int, _ c: Int) -> Bool {
            if r < 0 || r >= m || c < 0 || c >= n { return false }
            if grid[r][c] == 1 { return true }
            grid[r][c] = 1
            let up = dfs(r - 1, c), down = dfs(r + 1, c)
            let left = dfs(r, c - 1), right = dfs(r, c + 1)
            return up && down && left && right
        }
        var ans = 0
        for r in 0..<m {
            for c in 0..<n where grid[r][c] == 0 {
                if dfs(r, c) { ans += 1 }
            }
        }
        return ans
    }
}

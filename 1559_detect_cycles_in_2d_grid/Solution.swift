// LeetCode 1559 - Detect Cycles in 2D Grid
// https://leetcode.com/problems/detect-cycles-in-2d-grid/

class Solution {
    func containsCycle(_ grid: [[Character]]) -> Bool {
        let m = grid.count, n = grid[0].count
        var seen = Set<Int>()
        func key(_ r: Int, _ c: Int) -> Int { r * n + c }
        func dfs(_ r: Int, _ c: Int, _ pr: Int, _ pc: Int) -> Bool {
            seen.insert(key(r, c))
            for (dr, dc) in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                let nr = r + dr, nc = c + dc
                if nr < 0 || nr >= m || nc < 0 || nc >= n { continue }
                if grid[nr][nc] != grid[r][c] || (nr == pr && nc == pc) { continue }
                if seen.contains(key(nr, nc)) || dfs(nr, nc, r, c) { return true }
            }
            return false
        }
        for r in 0..<m {
            for c in 0..<n {
                if !seen.contains(key(r, c)) && dfs(r, c, -1, -1) { return true }
            }
        }
        return false
    }
}

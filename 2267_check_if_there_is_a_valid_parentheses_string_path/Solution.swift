// LeetCode 2267 - Check if There Is a Valid Parentheses String Path
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

class Solution {
    func hasValidPath(_ grid: [[Character]]) -> Bool {
        let m = grid.count, n = grid[0].count
        if (m + n - 1) % 2 == 1 || grid[0][0] == ")" || grid[m - 1][n - 1] == "(" { return false }
        var vis = Set<Int>()
        func dfs(_ r: Int, _ c: Int, _ bal: Int) -> Bool {
            if r >= m || c >= n { return false }
            let nb = bal + (grid[r][c] == "(" ? 1 : -1)
            if nb < 0 { return false }
            if r == m - 1 && c == n - 1 { return nb == 0 }
            let k = ((r * n + c) << 10) | nb
            if !vis.insert(k).inserted { return false }
            return dfs(r + 1, c, nb) || dfs(r, c + 1, nb)
        }
        return dfs(0, 0, 0)
    }
}

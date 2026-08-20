// LeetCode 1905 - Count Sub Islands
// https://leetcode.com/problems/count-sub-islands/

class Solution {
    func countSubIslands(_ grid1: [[Int]], _ grid2: [[Int]]) -> Int {
        var grid2 = grid2
        let rows = grid2.count, cols = grid2[0].count
        func dfs(_ r: Int, _ c: Int) -> Bool {
            if r < 0 || c < 0 || r >= rows || c >= cols || grid2[r][c] == 0 { return true }
            grid2[r][c] = 0
            var ok = grid1[r][c] == 1
            for (nr, nc) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] {
                if !dfs(nr, nc) { ok = false }
            }
            return ok
        }
        var ans = 0
        for r in 0..<rows {
            for c in 0..<cols {
                if grid2[r][c] == 1 && dfs(r, c) { ans += 1 }
            }
        }
        return ans
    }
}

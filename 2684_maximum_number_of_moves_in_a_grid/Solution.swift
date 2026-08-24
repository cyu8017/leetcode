// LeetCode 2684 - Maximum Number of Moves in a Grid
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution {
    func maxMoves(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var dp = Array(repeating: true, count: m)
        var ans = 0
        for c in 0..<(n - 1) {
            var nxt = Array(repeating: false, count: m)
            var moved = false
            for r in 0..<m where dp[r] {
                for nr in (r - 1)...(r + 1) where nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c] {
                    nxt[nr] = true
                    moved = true
                }
            }
            if !moved { break }
            dp = nxt
            ans += 1
        }
        return ans
    }
}

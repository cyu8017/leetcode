// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution {
    func countUnguarded(_ m: Int, _ n: Int, _ guards: [[Int]], _ walls: [[Int]]) -> Int {
        var grid = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for w in walls { grid[w[0]][w[1]] = 2 }
        for g in guards { grid[g[0]][g[1]] = 2 }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for g in guards {
            for d in dirs {
                var r = g[0] + d.0, c = g[1] + d.1
                while r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != 2 {
                    grid[r][c] = 1
                    r += d.0
                    c += d.1
                }
            }
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 0 { ans += 1 }
        }
        return ans
    }
}

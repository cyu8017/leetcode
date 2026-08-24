// LeetCode 2596 - Check Knight Tour Configuration
// https://leetcode.com/problems/check-knight-tour-configuration/

class Solution {
    func checkValidGrid(_ grid: [[Int]]) -> Bool {
        let n = grid.count
        if grid[0][0] != 0 { return false }
        var pos = [[Int]](repeating: [0, 0], count: n * n)
        for i in 0..<n {
            for j in 0..<n { pos[grid[i][j]] = [i, j] }
        }
        let dirs = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for v in 0..<(n * n - 1) {
            let r = pos[v][0], c = pos[v][1]
            var ok = false
            for d in dirs {
                if r + d.0 == pos[v + 1][0] && c + d.1 == pos[v + 1][1] {
                    ok = true
                    break
                }
            }
            if !ok { return false }
        }
        return true
    }
}

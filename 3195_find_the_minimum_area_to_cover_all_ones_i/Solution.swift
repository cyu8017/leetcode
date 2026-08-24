// LeetCode 3195 - Find the Minimum Area to Cover All Ones I
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution {
    func minimumArea(_ grid: [[Int]]) -> Int {
        var x1 = grid.count, y1 = grid[0].count, x2 = 0, y2 = 0
        for i in 0..<grid.count {
            for j in 0..<grid[0].count where grid[i][j] == 1 {
                x1 = min(x1, i); y1 = min(y1, j)
                x2 = max(x2, i); y2 = max(y2, j)
            }
        }
        return (x2 - x1 + 1) * (y2 - y1 + 1)
    }
}

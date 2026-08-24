// LeetCode 3128 - Right Triangles
// https://leetcode.com/problems/right-triangles/

class Solution {
    func numberOfRightTriangles(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var rows = Array(repeating: 0, count: m)
        var cols = Array(repeating: 0, count: n)
        for i in 0..<m {
            for j in 0..<n {
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
            }
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                ans += (rows[i] - 1) * (cols[j] - 1)
            }
        }
        return ans
    }
}

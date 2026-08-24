// LeetCode 0861 - Score After Flipping Matrix
// https://leetcode.com/problems/score-after-flipping-matrix/

class Solution {
    func matrixScore(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        for r in 0..<m where grid[r][0] == 0 {
            for j in 0..<n { grid[r][j] ^= 1 }
        }
        var ans = m * (1 << (n - 1))
        for j in 1..<n {
            var ones = 0
            for i in 0..<m { ones += grid[i][j] }
            ans += max(ones, m - ones) * (1 << (n - 1 - j))
        }
        return ans
    }
}

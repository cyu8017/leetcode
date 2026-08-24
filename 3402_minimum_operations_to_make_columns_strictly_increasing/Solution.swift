// LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
// https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var ans = 0
        for j in 0..<n {
            for i in 1..<m {
                if grid[i][j] <= grid[i - 1][j] {
                    let need = grid[i - 1][j] + 1
                    ans += need - grid[i][j]
                    grid[i][j] = need
                }
            }
        }
        return ans
    }
}

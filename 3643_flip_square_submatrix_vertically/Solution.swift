// LeetCode 3643 - Flip Square Submatrix Vertically
// https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution {
    func reverseSubmatrix(_ grid: [[Int]], _ x: Int, _ y: Int, _ k: Int) -> [[Int]] {
        var grid = grid
        if k >= 2 {
            for i in x..<(x + k / 2) {
                let i2 = x + k - 1 - (i - x)
                for j in y..<(y + k) {
                    let tmp = grid[i][j]
                    grid[i][j] = grid[i2][j]
                    grid[i2][j] = tmp
                }
            }
        }
        return grid
    }
}

// LeetCode 2319 - Check if Matrix Is X-Matrix
// https://leetcode.com/problems/check-if-matrix-is-x-matrix/

class Solution {
    func checkXMatrix(_ grid: [[Int]]) -> Bool {
        let n = grid.count
        for i in 0..<n {
            for j in 0..<n {
                let diag = i == j || i + j == n - 1
                if diag { if grid[i][j] == 0 { return false } }
                else if grid[i][j] != 0 { return false }
            }
        }
        return true
    }
}

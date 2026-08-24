// LeetCode 3142 - Check if Grid Satisfies Conditions
// https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution {
    func satisfiesConditions(_ grid: [[Int]]) -> Bool {
        let m = grid.count, n = grid[0].count
        for i in 0..<m {
            for j in 0..<n {
                let x = grid[i][j]
                if i + 1 < m && x != grid[i + 1][j] { return false }
                if j + 1 < n && x == grid[i][j + 1] { return false }
            }
        }
        return true
    }
}

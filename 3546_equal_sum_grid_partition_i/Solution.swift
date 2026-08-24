// LeetCode 3546 - Equal Sum Grid Partition I
// https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution {
    func canPartitionGrid(_ grid: [[Int]]) -> Bool {
        var s = 0
        for row in grid { for x in row { s += x } }
        if s % 2 != 0 { return false }
        let m = grid.count, n = grid[0].count
        var pre = 0
        for i in 0..<m {
            for x in grid[i] { pre += x }
            if pre * 2 == s && i + 1 < m { return true }
        }
        pre = 0
        for j in 0..<n {
            for i in 0..<m { pre += grid[i][j] }
            if pre * 2 == s && j + 1 < n { return true }
        }
        return false
    }
}

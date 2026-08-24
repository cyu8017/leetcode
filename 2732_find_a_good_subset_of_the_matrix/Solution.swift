// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

class Solution {
    func goodSubsetofBinaryMatrix(_ grid: [[Int]]) -> [Int] {
        let n = grid[0].count
        var first: [Int: Int] = [:]
        for i in grid.indices {
            var mask = 0
            for j in 0..<n where grid[i][j] == 1 { mask |= 1 << j }
            if mask == 0 { return [i] }
            for (key, value) in first where (key & mask) == 0 {
                return value < i ? [value, i] : [i, value]
            }
            if first[mask] == nil { first[mask] = i }
        }
        return []
    }
}

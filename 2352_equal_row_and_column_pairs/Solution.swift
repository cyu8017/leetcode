// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution {
    func equalPairs(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var freq: [String: Int] = [:]
        for row in grid {
            freq[row.map(String.init).joined(separator: ","), default: 0] += 1
        }
        var ans = 0
        for j in 0..<n {
            var col = [Int](repeating: 0, count: n)
            for i in 0..<n { col[i] = grid[i][j] }
            ans += freq[col.map(String.init).joined(separator: ","), default: 0]
        }
        return ans
    }
}

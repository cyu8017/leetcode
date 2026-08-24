// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution {
    func deleteGreatestValue(_ grid: [[Int]]) -> Int {
        var grid = grid.map { $0.sorted() }
        var ans = 0
        let n = grid[0].count
        for c in 0..<n {
            var mx = 0
            for row in grid { mx = max(mx, row[c]) }
            ans += mx
        }
        return ans
    }
}

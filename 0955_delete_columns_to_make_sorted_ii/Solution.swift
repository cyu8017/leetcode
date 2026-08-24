// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let rows = strs.map { Array($0) }
        let n = rows.count, m = rows[0].count
        var deleted = 0
        var sortedPair = Array(repeating: false, count: max(0, n - 1))
        for c in 0..<m {
            var bad = false
            for r in 0..<(n - 1) {
                if !sortedPair[r] && rows[r][c] > rows[r + 1][c] { bad = true; break }
            }
            if bad { deleted += 1; continue }
            for r in 0..<(n - 1) {
                if rows[r][c] < rows[r + 1][c] { sortedPair[r] = true }
            }
        }
        return deleted
    }
}

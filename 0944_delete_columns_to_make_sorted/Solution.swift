// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let rows = strs.map { Array($0) }
        let m = rows[0].count, n = rows.count
        var ans = 0
        for c in 0..<m {
            for r in 0..<(n - 1) {
                if rows[r][c] > rows[r + 1][c] { ans += 1; break }
            }
        }
        return ans
    }
}

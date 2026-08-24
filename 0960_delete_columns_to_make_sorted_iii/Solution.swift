// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
        let rows = strs.map { Array($0) }
        let m = rows[0].count
        var dp = Array(repeating: 1, count: m)
        for j in 0..<m {
            for i in 0..<j {
                var ok = true
                for row in rows where row[i] > row[j] { ok = false; break }
                if ok { dp[j] = max(dp[j], dp[i] + 1) }
            }
        }
        return m - (dp.max() ?? 0)
    }
}

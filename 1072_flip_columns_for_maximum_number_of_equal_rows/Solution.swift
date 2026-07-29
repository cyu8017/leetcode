// LeetCode 1072 - Flip Columns For Maximum Number of Equal Rows
// https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

class Solution {
    func maxEqualRowsAfterFlips(_ matrix: [[Int]]) -> Int {
        var patterns: [[Int]: Int] = [:]
        for row in matrix {
            let base = row[0]
            let key = row.map { $0 ^ base }
            patterns[key, default: 0] += 1
        }
        return patterns.values.max() ?? 0
    }
}

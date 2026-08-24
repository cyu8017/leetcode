// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

class Solution {
    func champagneTower(_ poured: Int, _ query_row: Int, _ query_glass: Int) -> Double {
        var row = [Double(poured)]
        if query_row == 0 { return min(1.0, row[query_glass]) }
        for r in 0..<query_row {
            var nextRow = Array(repeating: 0.0, count: r + 2)
            for i in 0..<row.count {
                let overflow = (row[i] - 1.0) / 2.0
                if overflow > 0 {
                    nextRow[i] += overflow
                    nextRow[i + 1] += overflow
                }
            }
            row = nextRow
        }
        return min(1.0, row[query_glass])
    }
}

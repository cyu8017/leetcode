// LeetCode 0006 - Zigzag Conversion
// https://leetcode.com/problems/zigzag-conversion/

class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        if numRows == 1 || numRows >= s.count {
            return s
        }

        var rows = Array(repeating: [Character](), count: numRows)
        var index = 0
        var step = 1

        for ch in s {
            rows[index].append(ch)
            if index == 0 {
                step = 1
            } else if index == numRows - 1 {
                step = -1
            }
            index += step
        }

        return String(rows.flatMap { $0 })
    }
}

// LeetCode 0498 - Diagonal Traverse
// https://leetcode.com/problems/diagonal-traverse/

class Solution {
    func findDiagonalOrder(_ mat: [[Int]]) -> [Int] {
        if mat.isEmpty || mat[0].isEmpty {
            return []
        }
        let rows = mat.count
        let cols = mat[0].count
        var result: [Int] = []
        var row = 0
        var col = 0
        var upward = true

        for _ in 0..<(rows * cols) {
            result.append(mat[row][col])
            if upward {
                if col == cols - 1 {
                    row += 1
                    upward = false
                } else if row == 0 {
                    col += 1
                    upward = false
                } else {
                    row -= 1
                    col += 1
                }
            } else if row == rows - 1 {
                col += 1
                upward = true
            } else if col == 0 {
                row += 1
                upward = true
            } else {
                row += 1
                col -= 1
            }
        }
        return result
    }
}

// LeetCode 0240 - Search a 2D Matrix II
// https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        if matrix.isEmpty || matrix[0].isEmpty {
            return false
        }
        var row = 0
        var col = matrix[0].count - 1
        while row < matrix.count && col >= 0 {
            let value = matrix[row][col]
            if value == target {
                return true
            }
            if value > target {
                col -= 1
            } else {
                row += 1
            }
        }
        return false
    }
}

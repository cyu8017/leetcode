// LeetCode 0074 - Search a 2D Matrix
// https://leetcode.com/problems/search-a-2d-matrix/

class Solution {
    func searchMatrix(_ matrix: [[Int]], _ target: Int) -> Bool {
        var row = 0
        var col = matrix[0].count - 1

        while row < matrix.count && col >= 0 {
            if matrix[row][col] == target {
                return true
            }
            if matrix[row][col] > target {
                col -= 1
            } else {
                row += 1
            }
        }

        return false
    }
}
